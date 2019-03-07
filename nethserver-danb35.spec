Summary: NethServer configuration for danb35 repository
%define name nethserver-danb35
%define version 1.0.0
%define release 4
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

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
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
