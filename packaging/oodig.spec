Name:           oodig
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign DNS lookup and resolver diagnostic utility in pure openOODA.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oodig
Source0:        oodig-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oodig is a sovereign, capability-bounded DNS lookup utility written
in pure openOODA, featuring zero ambient authority, standard DiG compatibility,
synthetic showcases, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oodig
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oodig-uninstall

%files
/usr/bin/oodig
/usr/bin/oodig-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign pure openOODA elevation with dual-surface CLI and MCP
