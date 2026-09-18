---
name: rhcsa-drill
description: Generates and grades RHCSA practice tasks against the UTM lab VMs. Exam-shaped, one objective at a time, graded by inspecting real system state rather than by asking what was typed.
disable-model-invocation: true
aliases: [drill]
---

# RHCSA drill

Generates exam-shaped practice tasks and grades them against real system state.

## Environment

Practice VMs run in UTM on Apple Silicon — aarch64, RHEL 10, Red Hat Developer Subscription.
Bridged on `mizutani` (reachable over LAN and WireGuard), shared networking on `darwin`.
`errata` on Proxmox is the spare slot if a VM needs to be on the LAN proper.

Never drill against `mikoshi`, `soulkiller`, `netwatch`, `erebus`, `sandevistan`, `kerenzikov`,
`netrunner`, or `edgerunner`. Those are prod.

## Running a drill

1. **Pick one objective.** Ask which, or pick the one least recently drilled. One at a time — the exam tests them in combination, but learning them works in isolation.
2. **State the task the way the exam does.** Terse, outcome-stated, no method prescribed. "Create a 2 GiB logical volume named `data` on `vg_lab`, formatted XFS, mounted persistently at `/srv/data`." Not "use lvcreate to...".
3. **Stop.** Do not show the solution, do not hint. Wait.
4. **Grade by inspection.** SSH to the VM and check actual state — `lsblk`, `findmnt`, `getenforce`, `firewall-cmd --list-all`, `systemctl is-enabled`. Never grade by asking what they typed.
5. **Report pass or fail per criterion**, with the command that proved it. On a fail, say which criterion and what the state actually was — then stop and let them fix it before showing anything.

## Objectives

| Area | Drills |
|------|--------|
| Users and groups | Local accounts, supplementary groups, password aging, sudo rules |
| Permissions | Standard modes, setgid directories, sticky bit, ACLs, umask |
| SELinux | Modes, file contexts, `restorecon`, booleans, port labeling |
| Storage | Partitions, LVM create/extend, filesystem resize, swap, persistent mounts |
| Networking | `nmcli` static addressing, hostname, `/etc/hosts`, name resolution |
| firewalld | Zones, services, ports, permanent versus runtime |
| systemd | Units, enabling, targets, timers, journal inspection |
| Software | `dnf`, repositories, module streams, verifying package ownership |
| Containers | Rootless podman, persistent storage, systemd-managed containers |
| Scheduling | `cron`, `at`, systemd timers |
| Boot | Rescue targets, resetting the root password, `grub2` changes |

## Rules

**Persistence counts.** An exam task is not complete if it does not survive a reboot. Grade it as failed if `/etc/fstab` or `systemctl enable` is missing, and say that is why.

**Exam mechanism first.** Where the exam expects a specific tool, drill that tool. If current practice differs, note it in one line after grading — never substitute it silently.

**No partial credit narration.** Pass or fail per criterion. "Almost" teaches nothing.

**Time it when asked.** The real exam is time-pressured. If they ask for timed mode, state the budget up front and report elapsed at the end.
