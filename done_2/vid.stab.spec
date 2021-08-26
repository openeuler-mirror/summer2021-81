%undefine __cmake_in_source_build
# https://github.com/georgmartius/vid.stab/commit/aeabc8daa7904f9edf7441a11f293965a5ef53b8
%global commit aeabc8daa7904f9edf7441a11f293965a5ef53b8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20190213

Name:           vid.stab
Version:        1.1.0
Release:        16.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Video stabilize library for fmpeg, mlt or transcode
License:        GPLv2+
URL:            http://public.hronopik.de/vid.stab
Source0:        https://github.com/georgmartius/vid.stab/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  orc-devel
Requires:       glibc
#To be removed more or less in Fedora 32
Provides:	%{name}-libs = %{version}-%{release}
Obsoletes:	%{name}-libs < %{version}-%{release}

%description
Vidstab is a video stabilization library which can be plugged-in with Ffmpeg
and Transcode.

%package devel
Summary:        Development files for vid.stab
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files (library and header files).

%prep
%setup -q -n %{name}-%{commit}
# remove SSE2 flags
sed -i 's|-DUSE_SSE2 -msse2||' tests/CMakeLists.txt
# fxi warning _FORTIFY_SOURCE requires compiling with optimization (-O)
sed -i 's|-Wall -O0|-Wall -O|' tests/CMakeLists.txt
# use macros EXIT_SUCCESS and EXIT_FAILURE instead for portability reasons.
sed -i 's|return units_failed==0;|return units_failed>0;|' tests/testframework.c

%build
%cmake
%cmake_build

# build the tests program
pushd tests
%cmake
%cmake_build
popd

%install
%cmake_install

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} tests/tests || :

%ldconfig_scriptlets -n %{name}

%files
%doc README.md
%license LICENSE
%{_libdir}/libvidstab.so.*

%files devel
%{_includedir}/vid.stab/
%{_libdir}/libvidstab.so
%{_libdir}/pkgconfig/vidstab.pc

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16.20190213gitaeabc8d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15.20190213gitaeabc8d
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Fix cmake build

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14.20190213gitaeabc8d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13.20190213gitaeabc8d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12.20190213gitaeabc8d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-11.20190213gitaeabc8d
- Update to 1.1.0-11.20190213gitaeabc8d

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10.20180529git38ecbaf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Sérgio Basto <sergio@serjux.com> - 1.1.0-9.20180529git38ecbaf
- Obsoletes: vid.stab-libs

* Sat Sep 29 2018 Sérgio Basto <sergio@serjux.com> - 1.1.0-1.20180529git38ecbaf
- Fix version number and update the source code

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5.20170830gitafc8ea9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4.20170830gitafc8ea9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1-3.20170830gitafc8ea9
- change license tag to GPLv2
- fix warning _FORTIFY_SOURCE requires compiling with optimization (-O)

* Sun Oct 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1-2.20170830gitafc8ea9
- use macros EXIT_SUCCESS and EXIT_FAILURE instead for portability reasons

* Sat Sep 30 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1-1.20170830gitafc8ea9
- Initial build rpm
