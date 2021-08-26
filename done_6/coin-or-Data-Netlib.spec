%global		module		Data-Netlib

Name:		coin-or-%{module}
Summary:	COIN-OR Netlib models
Version:	1.2.9
Release:	3%{?dist}
License:	EPL-1.0
URL:		https://projects.coin-or.org/svn/Data/Netlib
Source0:	https://www.coin-or.org/download/pkgsource/Data/%{module}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(zlib)

%description
This package contains the COmputational INfrastructure for Operations
Research (COIN-OR) models from netlib for testing.

%prep
%autosetup -n %{module}-%{version}

%build
%configure
%make_build

%install
%make_install pkgconfiglibdir=%{_datadir}/pkgconfig

%files
%{_datadir}/coin/
%{_datadir}/pkgconfig/coindatanetlib.pc

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Jerry James <loganjerry@gmail.com> - 1.2.9-1
- Version 1.2.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Jerry James <loganjerry@gmail.com> - 1.2.8-1
- Initial RPM
