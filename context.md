# arpatek — context

## Identity

- **Full name:** Juan Garcia
- **Handle:** arpatek
- **Role:** DevOps & Automation Engineer
- **Location:** California, USA
- **Languages:** English (fluent), Spanish (fluent)
- **Email:** juang.dev@proton.me
- **Public repos:** Codeberg (codeberg.org/arpatek)
- **Internal CI/CD:** Gitea self-hosted at soulkiller.home.arpa — not for public repos, pipelines only

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
| Shell | Zsh (Mac, Asahi) · Bash (servers) |
| Editor | Neovim + LazyVim (Mac, Asahi) · Vim (RHEL/servers) |
| Terminal | Ghostty (Asahi MacBook) · iTerm2 (Mac Mini) |

## Homelab

All VMs on Proxmox host blackwall. Cyberpunk 2077 naming theme throughout.
Buildout is complete for now — current focus is using it for cert study, coding practice,
DevOps and sysadmin practice rather than further expansion.

**Hypervisor**

| Host | IP | Role |
|------|----|------|
| blackwall | 10.33.111.44 | Proxmox VE |

**VMs**

| Host | IP | Role |
|------|----|------|
| mikoshi | 10.33.111.100 | FreeIPA — identity, Kerberos, DNS authority (home.arpa) |
| soulkiller | 10.33.111.101 | Gitea + act_runner CI + container registry |
| netwatch | 10.33.111.102 | PLG stack — Prometheus, Loki, Grafana |
| erebus | 10.33.111.103 | k3s control plane |
| sandevistan | 10.33.111.104 | k3s worker |
| kerenzikov | 10.33.111.105 | k3s worker |
| gonk-01 | 10.33.111.200 | Dev VM — reprovisioned as needed |
| gonk-02 | 10.33.111.201 | Dev VM — reprovisioned as needed |

**Infrastructure**

| Host | IP | Role |
|------|----|------|
| netrunner | 10.33.111.141 | Raspberry Pi — Pi-hole DNS/DHCP, WireGuard VPN server, NAS. The original Pi that started the homelab. |

**Network**
- LAN: 10.33.111.0/24, gateway 10.33.111.1
- WireGuard VPN: 10.10.10.0/24
- DNS domain: home.arpa
- DNS: FreeIPA (mikoshi) authoritative for home.arpa, Pi-hole (netrunner) for everything else
- Inbound firewall: only UDP 55055 (WireGuard)

**NAS**
- CIFS mount: //netrunner.home.arpa/NAS → /mnt/pi-nas
- Pi filesystem root: /srv/nas

**Personal devices**

| Device | Name | Notes |
|--------|------|-------|
| MacBook Air (Asahi Linux) | silverhand | CLI work, Claude Code, current daily driver |
| Mac Mini (macOS) | mizutani | Main stable workstation — GUI, macOS tooling |
| MacBook Air (macOS) | malorian | WireGuard peer |
| iPhone | uplink | WireGuard peer |
| iPad Mini | dataslab | WireGuard peer |

## Projects

| Repo | Lang | Description |
|------|------|-------------|
| home.arpa | Shell | Homelab IaC — configs, Ansible, k3s manifests, docs |
| dotfiles | Shell | Zsh, tmux, Neovim, Git, SSH — symlink-managed |
| mac-setup | Shell | macOS bootstrap — Homebrew, AeroSpace, LazyVim |
| terraform-xo | HCL | Provision VMs on XCP-ng via Xen Orchestra + cloud-init |
| arpatek.dev | Python | FastAPI portfolio — ASCII art for curl, terminal UI for browser, deployed on k3s |
| portal-22 | Python | SSH key + config generator — CLI single-key mode and bulk YAML mode, arpatek naming convention |
| citadel | Python | Pattern-based password generator with cryptographically secure entropy |
| ansible-baseline | Shell | Modular Ansible roles for provisioning Debian/Ubuntu dev environments |
| snaputil | Python | CLI system snapshot tool — CPU, memory, disk, network, rich TTY output |
| puppet-modules | Puppet | Modules for provisioning and hardening Debian VMs |
| cloudflare-ddns | Shell | Bash + systemd dynamic DNS updater for Cloudflare |
| devkit | Shell | Data-driven TUI launcher for homelab ops |

## Work history (abbreviated)

**Senior Test Technician — TrueNAS (iXsystems), 2021–2024**
Built a 22,000+ line Bash/Python automation suite (CC & SWQC) for manufacturing QC.
Automated BIOS, firmware, and hardware validation via IPMI and Redfish API for 16+ server types simultaneously. Developed Python Redfish API clients for BIOS push/export on liquid immersion platforms. Integrated with PBS archive servers and PostgreSQL for burn-in parsing and reporting.
