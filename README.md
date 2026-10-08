# oodig: Sovereign DNS LOOKUP

<div align="center">

```
================================================================================
                                oodig
               Sovereign openOODA DNS LOOKUP
================================================================================
```

**Sovereign DNS LOOKUP**  
*Comprehensive DNS lookup utility querying specific record types (A, AAAA, MX, TXT).*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openOODA-tools.github.io/oodig/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oodig-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openOODA-tools.github.io/oodig/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openOODA-tools.github.io/oodig/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oodig-uninstall
# or: curl -fsSL https://openOODA-tools.github.io/oodig/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oodig [@server] [-p port] [name] [type] [options]

Sovereign DNS lookup and resolver diagnostic utility in pure openOODA.

Query Options:
  @server              Server to query (IP or hostname)
  -p port              Port number to query [default: 53]
  -x ip                Reverse lookup helper (in-addr.arpa)
  +short               Concise output mode
  +trace               Recursive root-to-authoritative trace
  +tcp                 Use TCP instead of UDP
  +dnssec              Request DNSSEC records (DO bit)
  -D, --demo           Run synthetic multi-record DNS query showcase

General Options:
  -h, --help           Display this help and exit
  -v, --version        Output version information and exit
  -j, --json           Output formatted as JSON
      --color <WHEN>   Colorize output: auto, always, never [default: auto]
      --theme <NAME>   Override active oote palette
      --mcp            Run as Model Context Protocol stdio server
```

---

## 3. Theming Integration (`oote`)

`oodig` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oodig` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

* `dig_query`: Perform standard DNS query for domain name and record type (A, AAAA, MX, TXT, NS, CNAME, SOA, PTR).
* `dig_resolve`: High-level name resolution returning concise address list.
* `dig_reverse`: Reverse DNS lookup for an IPv4 address to PTR domain.
* `dig_trace`: Hierarchical DNS resolution trace from root servers to authoritative answers.
* `dig_inspect_nameserver`: Inspect local resolver configuration from systemd-resolved / resolv.conf.
* `dig_demo`: Return complete synthetic showcase demonstrating diverse DNS answer sections.

```bash
oodig --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (&NetCap, &TlsCap, &McpCap). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
