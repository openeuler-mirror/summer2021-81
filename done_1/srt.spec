Name:           srt
Version:        1.4.2
Release:        4%{?dist}
Summary:        Secure Reliable Transport protocol tools

License:        MPLv2.0
URL:            https://www.srtalliance.org
Source0:        https://github.com/Haivision/srt/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-gcc11.patch

BuildRequires: make
BuildRequires:  cmake gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel

Requires: srt-libs%{?_isa} = %{version}-%{release}


%description
Secure Reliable Transport (SRT) is an open source transport technology that
optimizes streaming performance across unpredictable networks, such as 
the Internet.

%package libs
Summary: Secure Reliable Transport protocol libraries

%description libs
Secure Reliable Transport protocol libraries

%package devel
Summary: Secure Reliable Transport protocol development libraries and headers
Requires: srt-libs%{?_isa} = %{version}-%{release}

%description devel
Secure Reliable Transport protocol development libraries and header files


%prep
%autosetup -p1


%build
%cmake \
  -DENABLE_STATIC=OFF \
  -DENABLE_UNITTESTS=ON \
  -DENABLE_GETNAMEINFO=ON \
  -DUSE_ENCLIB=gnutls

%cmake_build


%install
%cmake_install
# remove old upstream temporary compatibility pc
rm -f %{buildroot}/%{_libdir}/pkgconfig/haisrt.pc


%check
# Fails with x390x
make test \
%ifarch s390x
  || :
%endif


%ldconfig_scriptlets libs


%files
%license LICENSE
%doc README.md docs
%{_bindir}/srt-ffplay
%{_bindir}/srt-file-transmit
%{_bindir}/srt-live-transmit
%{_bindir}/srt-tunnel
%{_bindir}/test-srt

%files libs
%license LICENSE
%{_libdir}/libsrt.so.1*

%files devel
%doc examples
%{_includedir}/srt
%{_libdir}/libsrt.so
%{_libdir}/pkgconfig/srt.pc


%changelog
* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.4.2-4
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Jeff Law <law@redhat.com> - 1.4.2-2
- Fix missing #includes for gcc-11

* Thu Oct 29 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 1.4.1-4
- Use __cmake_in_source_build 

* Mon Apr 06 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4.1-3
- Switch to gnutls instead of openssl
- Enable tests
- Enforce strict EVR from main to -libs

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  9 2019 Yanko Kaneti <yaneti@declera.com> - 1.4.1-1
- Update to 1.4.1

* Mon Sep 16 2019 Yanko Kaneti <yaneti@declera.com> - 1.4.0-1
- Update to 1.4.0

* Wed Sep 11 2019 Yanko Kaneti <yaneti@declera.com> - 1.3.4-1
- Update to 1.3.4

* Thu Aug  1 2019 Yanko Kaneti <yaneti@declera.com> - 1.3.3-3
- First attempt
- Adjustments suggested by review
