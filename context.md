# arpatek — context

## Identity

- **Full name:** Juan Garcia
- **Handle:** arpatek
- **Role:** DevOps & Automation Engineer
- **Location:** California, USA
- **Languages:** English (fluent), Spanish (fluent)
- **Email:** juang.dev@proton.me
- **Public repos:** Codeberg (codeberg.org/arpatek), mirrored to GitHub (github.com/arpatek)
- **Internal CI/CD:** Gitea self-hosted at `soulkiller` — pipelines only, not for public repos

## Certifications

| Cert | Status |
|------|--------|
| RHCSA | In progress |
| RHCE | Roadmap |
| Terraform Associate | Roadmap |
| CKA | Roadmap |
| CKS | Roadmap |
| AWS | Roadmap |
| Google IT Automation with Python | Completed |
| Google IT Support | Completed |

## Current focus

- RHCSA in progress → RHCE → Terraform Associate → CKA → CKS → AWS
- Homelab: buildout complete, now the practice ground for cert study and DevOps work
- Deepening DevOps breadth across the full stack
- Long horizon: security — "hacker" in the original curious sense, not the job title

## Stack

| Layer | Tools |
|-------|-------|
| IaC | Terraform, Ansible, Puppet |
| Containers | k3s (Kubernetes), Docker |
| Languages | Bash, Python, HCL |
| Identity | FreeIPA / Kerberos |
| Monitoring | Prometheus, Loki, Grafana, Alloy, node_exporter |
| DNS/DHCP | Pi-hole |
| VPN | WireGuard |
| CI/CD | Gitea + act_runner |
| Systems | Linux (RHEL, Ubuntu, Debian, TrueNAS/FreeBSD) |
| Low-level | ZFS, SAS/HBA, BIOS, IPMI, Redfish API |
| Tools | Git, tmux, SSH |

## Daily tooling

| Tool | Where |
|------|-------|
| Shell | Zsh (macOS) · Bash (servers) |
| Editor | Neovim + LazyVim (macOS) · Vim (RHEL/servers) |
| Terminal | Ghostty |

## Homelab

All VMs on Proxmox host `blackwall`. Cyberpunk 2077 naming theme throughout.
Buildout is complete — current focus is using it for cert study, coding practice, and
DevOps/sysadmin practice rather than further expansion.

**Topology is not duplicated here.** Hosts, addressing, network layout, and the service map
live in [`home.arpa/docs/`](https://codeberg.org/arpatek/home.arpa/src/branch/main/docs)
(`hostnames.md`, `network.md`, `architecture.md`). That repo is the source of truth.

Services in the lab: FreeIPA (identity, Kerberos, DNS authority for `home.arpa`), Gitea +
act_runner (CI and container registry), Prometheus/Loki/Grafana, k3s (one control plane, two
workers), Pi-hole (DNS/DHCP), WireGuard, and CIFS NAS shares on two Raspberry Pis.

**Practice VMs**

RHCSA and lab practice VMs run in UTM on Apple Silicon rather than on Proxmox — `blackwall`
has only one spare slot. Virtualize (not Emulate), aarch64 images, RHEL 10 via the free Red
Hat Developer Subscription. Bridged on `mizutani` so they are reachable over LAN and
WireGuard; shared networking on `darwin`, since bridged over Wi-Fi is unreliable.

## Personal devices

| Device | Name | Notes |
|--------|------|-------|
| MacBook Air (macOS) | darwin | Main workstation — CLI work, Claude Code, 2 aarch64 RHEL VMs on UTM |
| Mac Mini (macOS) | mizutani | Dedicated UTM hypervisor — 4 bridged lab VMs |
| iPhone | uplink | WireGuard peer |
| iPad Mini | dataslab | WireGuard peer |

## Projects

| Repo | Lang | Description |
|------|------|-------------|
| home.arpa | Shell | Homelab IaC — configs, Ansible, k3s manifests, docs |
| arpa-iac | Shell | Ansible inventory and vault-backed credentials for home.arpa |
| dotfiles | Shell | Cross-platform (Linux + macOS) — Zsh, tmux, Neovim, Git, SSH; OS-aware installer, symlink-managed |
| terraform-xo | HCL | Provision VMs on XCP-ng via Xen Orchestra + cloud-init |
| arpatek.dev | Python | FastAPI portfolio — ASCII art for curl, terminal UI for browser, deployed on k3s |
| portal-22 | Python | SSH key + config generator — CLI single-key mode and bulk YAML mode, arpatek naming convention |
| citadel | Python | Pattern-based password generator with cryptographically secure entropy |
| ansible-baseline | Shell | Modular Ansible roles for provisioning Debian/Ubuntu dev environments |
| snaputil | Python | CLI system snapshot tool — CPU, memory, disk, network, rich TTY output |
| puppet-modules | Puppet | Modules for provisioning and hardening Debian VMs |
| cloudflare-ddns | Shell | Bash + systemd dynamic DNS updater for Cloudflare |
| devkit | Python | Data-driven TUI launcher for homelab ops |
| ai-soul | Shell | This repo — persona config, style guide, and Ollama Modelfile |

## Work history (abbreviated)

**Senior Test Technician — TrueNAS (iXsystems), 2021–2024**
Built a 22,000+ line Bash/Python automation suite (CC & SWQC) for manufacturing QC.
Automated BIOS, firmware, and hardware validation via IPMI and Redfish API for 16+ server types simultaneously. Developed Python Redfish API clients for BIOS push/export on liquid immersion platforms. Integrated with PBS archive servers and PostgreSQL for burn-in parsing and reporting.
