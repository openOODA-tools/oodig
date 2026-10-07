Name:           oodig
Version:        0.1.0
Release:        1%{?dist}
Summary:        Comprehensive DNS lookup utility querying specific record types (A, AAAA, MX, TXT).
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oodig
Source0:        oodig-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oodig is a sovereign, capability-bounded DNS LOOKUP written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oodig
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oodig-uninstall

%files
/usr/bin/oodig
/usr/bin/oodig-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
