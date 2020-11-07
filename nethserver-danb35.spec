Summary: NethServer configuration for danb35 repository
%define name nethserver-danb35
%define version 1.1.0
%define release 1
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: https://wiki.nethserver.org/doku.php?id=danb35_repository
BuildRequires: nethserver-devtools

AutoReq: no

%description
NethServer configuration for danb35 repository

%prep
%setup

%post

%preun

%build
%{makedocs}
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/
chmod +x %{buildroot}/usr/libexec/nethserver/api/%{name}/*

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
%attr(0755,root,root) %{_sysconfdir}/cron.daily/check4danb35Updates
%config(noreplace) /etc/yum.repos.d/danb35.repo

%changelog
* Sat Nov  7 2020 Dan Brown <dan@familybrown.org> - 1.1.0-1.ns7
- Give link and status in Cockpit

* Thu Jul  2 2020 Dan Brown <dan@familybrown.org> - 1.0.0-8.ns7
- Enable repo even when server has a subscription

* Sat Mar 28 2020 Dan Brown <dan@familybrown.org> - 1.0.0-7.ns7
- Changed definitions of GPG keys

* Fri Jun 14 2019 Dan Brown <dan@familybrown.org> - 1.0.0-6.ns7
- Enable danb35 repo with software-repos-save

* Thu Mar 21 2019 Dan Brown <dan@familybrown.org> - 1.0.0-5.ns7
- Add link to repoview to notification email

* Thu Mar  7 2019 Dan Brown <dan@familybrown.org> - 1.0.0-4.ns7
- Make check4updates script executable
- Add missing " in check4updates script

* Wed Jan 23 2019 Dan Brown <dan@familybrown.org> - 1.0.0-3.ns7
- Add second signing key
- Add daily check for updates
- Check for signed repo data

* Wed Jun 13 2018 Dan Brown <dan@familybrown.org> - 1.0.0-2.el7
- Corrected URL

* Sun Jun 10 2018 Dan Brown <dan@familybrown.org> - 1.0.0-1-ns7
- Initial release, based on nethserver-stephdl
