Name:           vmaf
Version:        2.1.1
Release:        1%{?dist}
Summary:        Video Multi-Method Assessment Fusion

License:        BSD-2-Clause-Patent
URL:            https://github.com/netflix/vmaf
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# This project relies on AVX
ExclusiveArch:  x86_64

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  nasm
BuildRequires:  vim-common


# Enforce our own build version for library
Requires:       libvmaf%{?_isa} = %{version}-%{release}
# Upstream only provides a static library
# Packages using libvmaf must Requires this:
#%%{?libvmaf_version:Requires: libvmaf%%{?_isa} = %%{libvmaf_version}}


%description
VMAF is a perceptual video quality assessment algorithm developed by
Netflix. VMAF Development Kit (VDK) is a software package that contains
the VMAF algorithm implementation, as well as a set of tools that allows
a user to train and test a custom VMAF model. For an overview, read this
tech blog post, or this slide deck.

https://github.com/Netflix/vmaf/blob/master/resource/doc/VMAF_ICIP17.pdf


%package -n     libvmaf
Summary:        Library for %{name}
Provides:       bundled(libsvm) = 3.24
#Some repo provides it
Provides: %{name}-static = %{version}-%{release}
Obsoletes: %{name}-static < %{version}-%{release}

%description -n libvmaf
Library for %{name}.

%package -n     libvmaf-devel
Summary:        Development files for %{name}
Requires:       libvmaf%{?_isa} = %{version}-%{release}
#Some repo provides it
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{name}-devel < %{version}-%{release}

%description -n libvmaf-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1
# Unbundle
rm -rf third_party/

%build
pushd libvmaf
%meson \
 -Ddefault_library=shared
%meson_build
popd

%install
pushd libvmaf
%meson_install
popd

#RPM Macros support
mkdir -p %{buildroot}%{rpmmacrodir}
cat > %{buildroot}%{rpmmacrodir}/macros.%{name} << EOF
# libvmaf RPM Macros
%libvmaf_version	%{version}
EOF
touch -r LICENSE %{buildroot}%{rpmmacrodir}/macros.%{name}

%check
pushd libvmaf
ninja -vC %{_vpath_builddir} test
popd

%ldconfig_scriptlets -n libvmaf


%files
%doc FAQ.md README.md
%{_bindir}/vmaf

%files -n libvmaf
%doc CHANGELOG.md
%license LICENSE
%{_libdir}/*.so.1*

%files -n libvmaf-devel
%doc CONTRIBUTING.md
%{rpmmacrodir}/macros.%{name}
%{_includedir}/libvmaf/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvmaf.pc


%changelog
* Wed Mar 10 2021 Leigh Scott <leigh123linux@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.3-1
- Update to 1.5.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.1-4
- Add upstream commit to mark ABI as C

* Sat May 23 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.1-3
- Fix pkconfig version

* Wed Mar 04 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.1-2
- Use shared for vmafossexec

* Tue Mar 03 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.15-1
- Update to 1.3.15

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-2.20190403git8f41503
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 06 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.3.14-1.20190403git8f415036
- Update to 1.3.14
- Rebase patches

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-2.20180914gita654f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.9-0.20180914gita654f6f
- Update to 1.3.9 up to 20180914

* Sat Apr 07 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.3-1.20180407git510e257
- Initial spec file
