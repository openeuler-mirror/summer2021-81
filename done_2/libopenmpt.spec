Name: libopenmpt
Version: 0.5.8
Release: 1%{?dist}

%global tar_root %{name}-%{version}+release.autotools

License: BSD
Summary: C/C++ library to decode tracker music module (MOD) files

URL: https://lib.openmpt.org/libopenmpt/

Source0: https://lib.openmpt.org/files/libopenmpt/src/%{tar_root}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: chrpath
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(zlib)

# for command-line player audio output
BuildRequires: pulseaudio-libs-devel
# don't build with niche options
#BuildRequires: portaudio-devel
#BuildRequires: SDL-devel
#BuildRequires: SDL2-devel

%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: devtoolset-8-toolchain
%endif

%description
libopenmpt is a cross-platform C++ and C library to decode tracked music
files (modules) into a raw PCM audio stream.

libopenmpt is based on the player code of the OpenMPT project (Open
ModPlug Tracker). In order to avoid code base fragmentation, libopenmpt is
developed in the same source code repository as OpenMPT.


%package -n openmpt123
Summary: Command-line tracker music player based on libopenmpt
Group: Applications/Multimedia
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n openmpt123
Openmpt123 is a cross-platform command-line or terminal based player
for tracker music (MOD) module files.


%package devel
Summary: Development files for the libopenmpt library
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files needed when building software which uses libopenmpt.


%prep
%autosetup -p1 -n %{tar_root}
sed -i 's/\r$//' LICENSE


%build
%if 0%{?rhel} && 0%{?rhel} < 8
. /opt/rh/devtoolset-8/enable
%endif

%configure  \
  --disable-static  \
  --without-sdl --without-sdl2 \
  --without-portaudio --without-portaudiocpp
make %{?_smp_mflags}


%install
%make_install
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
chrpath --delete ${RPM_BUILD_ROOT}%{_bindir}/openmpt123


%files -n openmpt123
%{_bindir}/openmpt123
%{_mandir}/man1/*

%files
%license LICENSE
%{_libdir}/*.so.0*
%{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/examples

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_docdir}/%{name}/examples/


%changelog
* Fri Apr 30 2021 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.8-1
- update to 0.5.8 (security release for the 0.5 series)

* Fri Apr  2 2021 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.7-1
- update to 0.5.7 (security release for the 0.5 series)

* Thu Feb 18 2021 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.5-1
- update to 0.5.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.4-1
- update to 0.5.4

* Thu Oct 29 2020 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.3-1
- upgrade to 0.5.3 (security release for the 0.5 series)

* Thu Oct 29 2020 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4.15-1
- update to 0.4.15

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4.11-1
- update to 0.4.11

* Fri Dec 20 2019 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4.10-2
- spec modifications as per Fedora reviewer comment in rhbz #1768408
- remove RPATH from openmpt123

* Mon Nov  4 2019 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4.10-1
- update to 0.4.10

* Sat Jun 01 2019 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4.5-1
- update to 0.4.5

* Sun Apr 21 2019 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4.4-1
- update to 0.4.4

* Sat Feb 23 2019 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4.3-1
- security update 0.4.3

* Sun Dec 30 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4.0-1
- initial package for libopenmpt 0.4.0
