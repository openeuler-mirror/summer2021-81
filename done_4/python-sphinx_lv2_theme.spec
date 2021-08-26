%global pypi_name sphinx_lv2_theme

%global common_description %{expand:
This is a minimal pure-CSS theme for Sphinx that uses the documentation
style of the LV2 plugin specification and related projects.

This theme is geared toward producing beautiful API documentation for C, C++,
and Python that is documented using the standard Sphinx domains.
The output does not use Javascript at all, and some common features are not
implemented, so this theme should not be considered a drop-in replacement
for typical Sphinx themes.}


Name:           python-%{pypi_name}
Version:        1.0.0
Release:        3%{?dist}
Summary:        A minimal pure-CSS theme for Sphinx
License:        ISC
URL:            https://gitlab.com/lv2/%{pypi_name}
Source0:        %{url}/-/archive/v%{version}/%{pypi_name}-v%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description %{common_description}


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

%if 0%{?epel} && 0%{?epel} <= 8
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%endif

%if 0%{?fedora} == 32
%py_provides python3-%{pypi_name}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name} %{common_description}


%prep
%autosetup -p1 -n %{pypi_name}-v%{version}


%build
%py3_build


%install
%py3_install


%files -n  python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
# For noarch packages: sitelib
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 15:54:29 CET 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.0.0-2
- Spec cleanup

* Fri Jan 15 08:38:05 CET 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.0.0-1
- Initial package release
