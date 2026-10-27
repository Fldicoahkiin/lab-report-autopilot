# Evidence and screenshots

## Build an evidence plan

Create one row per result that the report will claim:

| ID | Claim | Action | Visible proof | App/host | Planned caption |
| --- | --- | --- | --- | --- | --- |
| E01 | Database query returned three rows | Run the final SELECT | Query text, result grid, and row count | SSMS on Windows | 图1 查询条件及返回结果 |

Do not draft a success claim until its proof exists.

## Capture the right state

- Capture the result after the action completes.
- Include enough application context to identify the software and target.
- Keep the command, relevant parameters, and result visible together when possible.
- For GUI configuration, capture the final field values and the resulting behavior, not only the settings dialog.
- For a simple experiment, keep two to four figures that cover the main procedure and result.
- For professional practice, use four to six figures only when each one proves a different work stage. A useful sequence is visible task result, artifact properties, complete operation, field-level verification, and final result.
- Keep planned figure counts and evidence sequencing in working notes. Do not announce them in the submitted report.
- Preserve failed-state screenshots in working files only when they explain an adaptation. Do not place a resolved permission or startup error in the finished report unless it affects the result.
- Use a clear filename sequence such as `01-environment.png`, `02-query-result.png`, and `03-verification.png`.

Avoid:

- screenshots with no explanation;
- repeated images for different claims;
- tiny two-column figures whose text cannot be read at 100% page zoom;
- full-desktop captures containing irrelevant messages or personal files;
- cropped images that hide the command, target, error, or result needed to verify the claim;
- generated, downloaded, or borrowed images presented as execution evidence.

<a id="capture-techniques"></a>
## Capture techniques

### Capture one window, not the desktop

| Where | Tool |
| --- | --- |
| macOS host | `screencapture -x -o -l <window-id>`; get the window ID from `CGWindowListCopyWindowInfo`. The calling process needs Screen Recording permission. |
| Linux guest, X11 | `import -window <id> out.png` (ImageMagick) with the ID from `xdotool search --onlyvisible --class <app>`; `import -window root` for the full guest screen |
| Linux guest, Wayland | Switch the display manager to Xorg first (`WaylandEnable=false` in GDM) when scripted capture or `xdotool` is needed |
| Agent computer use | The tool's own screenshot; crop a working copy to the target window |

A capture of a VM window from the host shows the guest frame and its title; a capture from inside the guest shows only guest windows. Use the host capture when the virtualization product or guest name matters, and the guest capture for terminals and applications.

### Prepare the screen before capturing

- Size the terminal so the whole result fits: about 90–110 columns, 25–35 rows, a 12 pt monospace font. Enlarge the window rather than shrinking the font.
- Close update notifiers, welcome wizards, and notification banners. On Ubuntu, set `Prompt=never` in `/etc/update-manager/release-upgrades` and mark first-run setup done.
- Disable screen lock and blanking for the session so long steps do not end on a lock screen.
- A Chinese input method in the guest (ibus or fcitx with pinyin) swallows or rewrites text sent by `xdotool type`. Stop it for the session, or start the terminal with `GTK_IM_MODULE=gtk-im-context-simple XMODIFIERS=@im=none`, and type a test string before the real command. Restore the input method afterwards.
- Remove noise before the step that produces it, for example create macOS tar archives with `COPYFILE_DISABLE=1 tar --no-xattrs` so Linux `tar` does not print a screen of extended-header warnings.

### Keep the command in the frame

- Send `clear` as its own command, then the command to capture. `clear; command` on one line wipes the command itself.
- Show the command and its key result in one figure. Split long output into two figures, each starting with the command that produced it, instead of scrolling the command out of view.
- Prefer short command lines. Move long scripts into a file and show `bash script.sh` or the relevant lines.
- In interactive shells such as `mininet>`, use the shell's own clear (`sh clear`) and type subcommands one by one so each prompt stays visible.

### Wait for the result before capturing

- Detect completion from the program, not from a fixed sleep: a marker file written after the command, the returning prompt, or the absence of the process.
- `pgrep -f pattern` run over SSH also matches the SSH command line that contains `pattern`. Use `pgrep -x name`, a narrower pattern, or a marker file.
- After a GUI action, capture once to confirm the state changed before capturing the figure.

### Drive GUI programs reliably

- Some programs act only on the selected object; Tk-based tools such as MiniEdit open a node's Properties only after the node is left-clicked first.
- Menus need the pointer to move onto the item before the click registers. Take a screenshot of the open menu to locate the item instead of guessing offsets from another menu.
- Programs started with `sudo` need the display variables: `sudo -E` keeps `DISPLAY` and `XAUTHORITY`.
- After each dialog closes, the next click may only focus the main window. Confirm with a capture before continuing.
- When a toolbar button does not respond, use the same command from the menu bar; MiniEdit's Run button sometimes ignores synthetic clicks while Run → Run works.
- Keep one instance of the program. Before relaunching, close or kill earlier instances so captures do not show a stale window.

### Crop and keep evidence consistent

- Crop drop shadows and long empty terminal areas on the working copy; keep the original untouched.
- When the environment changes after a figure was taken, such as a renamed VM, a new IP address, or a re-uploaded file, retake every figure that shows the old value.

## Preserve and sanitize

1. Keep the original capture unchanged.
2. Work on a copy if cropping or redaction is needed.
3. Redact credentials, tokens, private hostnames, customer data, internal repository names, and unrelated personal notifications.
4. Keep non-sensitive values visible when they are required to understand the experiment.
5. Never blur a value and then quote it as if the reader could verify it.
6. Do not upload sensitive screenshots to third-party tools without specific user approval.

## Verify the evidence set

Run:

```text
"$PYTHON" "$SKILL_DIR/scripts/evidence_manifest.py" evidence/original \
  --output evidence-manifest.json
```

Review:

- every file opens and `error_count` is 0;
- width and height are adequate for the intended placement;
- duplicate hashes are either removed or justified;
- filenames match the planned order;
- each claim maps to one or more files;
- timestamps, host roles, IP addresses, and versions agree with the notes.

## Place figures in the report

- Put a figure directly after the paragraph that introduces it.
- Use a short factual caption that states what the reader should verify.
- Refer to the visible value in the following observation.
- Preserve aspect ratio.
- Use one large figure instead of two small figures when terminal or UI text would otherwise become unreadable.
- Crop empty margins, but retain application and target context.
- Number figures in first-reference order.
- For a full-flow packet figure, leave enough list height to show the connection sequence. For request or response figures, favor the decoded-field pane.
- When a saved artifact matters to the judgment, capture its properties or statistics: filename, interface, capture filter, packet count, drops, checksum, query row count, build result, or equivalent integrity signal.
- Keep every figure in one value system. Do not combine evidence from separate runs when addresses, ports, filenames, versions, timestamps, or task identifiers differ.

An explanation should read like:

> 在查询窗口执行筛选语句后，结果区返回 3 条记录，如图 2 所示。结果中的课程号均为 `C03`，说明连接条件和筛选条件同时生效。

Do not write only “运行结果如下” or “截图如下”.
