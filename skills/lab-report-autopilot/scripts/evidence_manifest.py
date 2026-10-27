from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError


EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(root: Path) -> dict[str, object]:
    if not root.is_dir():
        raise NotADirectoryError(f"evidence directory not found: {root}")

    files = sorted(
        path for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in EXTENSIONS
    )
    first_by_hash: dict[str, str] = {}
    images: list[dict[str, object]] = []

    for path in files:
        digest = sha256(path)
        entry: dict[str, object] = {
            "path": str(path.relative_to(root)),
            "bytes": path.stat().st_size,
            "sha256": digest,
        }
        try:
            with Image.open(path) as image:
                image.verify()
            # verify() checks chunk checksums but skips JPEG data and leaves the
            # image unusable, so reopen it and decode the pixels as well.
            with Image.open(path) as image:
                image.load()
                entry.update(width=image.width, height=image.height, format=image.format)
        # Pillow reports a broken PNG chunk as SyntaxError.
        except (UnidentifiedImageError, OSError, SyntaxError) as error:
            entry["error"] = str(error)
        if digest in first_by_hash:
            entry["duplicate_of"] = first_by_hash[digest]
        else:
            first_by_hash[digest] = entry["path"]
        images.append(entry)

    return {
        "root": str(root.resolve()),
        "image_count": len(images),
        "duplicate_count": sum("duplicate_of" in image for image in images),
        "error_count": sum("error" in image for image in images),
        "images": images,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_manifest(args.root)
    manifest = json.dumps(result, ensure_ascii=False, indent=2)

    if args.output:
        args.output.write_text(manifest + "\n", encoding="utf-8")
    else:
        print(manifest)
    if result["error_count"]:
        sys.exit(f"{result['error_count']} unreadable image(s); see the error fields")


if __name__ == "__main__":
    main()
