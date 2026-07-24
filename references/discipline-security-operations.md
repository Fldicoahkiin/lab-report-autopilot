# Security operations and local cyber ranges

## Scope

Use only local virtual machines, course ranges, deliberately vulnerable images, synthetic logs, or systems the user is authorized to test. Keep the network isolated when an exercise includes vulnerable services or malware-like indicators.

Read [confidential-work.md](confidential-work.md) when the task comes from workplace experience.

## Safe practice themes

- endpoint and asset inventory;
- suspicious outbound-connection review;
- alert timeline reconstruction;
- false-positive reasoning;
- weak-password discovery and remediation in a self-owned lab;
- service exposure review;
- log collection and incident notes;
- patch and configuration verification.

Do not reproduce a real customer event. Create a new local scenario with synthetic indicators.

## Environment route

- Use macOS Terminal for local inventory, hashing, DNS, connection, and packet-analysis work.
- Use Kali in Parallels for Linux security tools and an isolated analyst host.
- Use a Windows guest for Defender, Event Viewer, PowerShell, registry, service, or endpoint screenshots.
- Record VM network mode, snapshots, host roles, IP addresses, test accounts, and the authorized target range.

## Evidence sequence

1. Scope and environment.
2. Initial indicator or alert.
3. Host, process, user, network, and time context.
4. Verification using a second data source.
5. Decision: true positive, benign activity, false positive, or unresolved.
6. Containment or configuration change when the exercise permits it.
7. Post-change verification.

## Minimum evidence

- Authorized target and lab boundary.
- Original synthetic indicator.
- Commands or UI used to investigate it.
- A short timeline.
- Decision criteria.
- Before/after verification.

## Professional-practice reporting

Separate:

- general duties confirmed by the user;
- a local reproduction that demonstrates the method;
- public guidance or company facts with current citations.

Use screenshots from the reproduction and label them as such. Never imply that local evidence came from a production endpoint.
