Summary: NethServer configuration for danb35 repository
Name: nethserver-danb35
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.bz2
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
* Sun Jun 10 2018 Dan Brown <dan@familybrown.org> - 1.0.0-1-ns7
- Initial release, based on nethserver-stephdl
