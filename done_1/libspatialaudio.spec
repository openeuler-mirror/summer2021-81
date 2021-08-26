%global commit0 d926a2ee469a3fefd50a9364fb9ac6fb484c3f70
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20200406

Name:           libspatialaudio
Version:        3.1
Release:        4.%{date0}git%{?shortcommit0}%{?dist}
Summary:        Ambisonic encoding / decoding and binauralization library

License:        LGPLv2+
URL:            https://github.com/videolabs/libspatialaudio
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libmysofa)


%description
libspatialaudio is an open-source and cross-platform C++ library for
Ambisonic encoding and decoding, filtering and binaural rendering. It is
targetted to render High-Order Ambisonic (HOA) and VR/3D audio samples
in multiple environments, from headphones to classic loudspeakers. Its
binaural rendering can be used for classical 5.1/7.1 spatial channels
as well as Ambisonics inputs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit0}


%build
%cmake3 \
  -DBUILD_STATIC_LIBS=OFF

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets


%files
%license LICENSE
%doc README.md
%{_libdir}/libspatialaudio.so.1*

%files devel
%{_includedir}/*
%{_libdir}/libspatialaudio.so
%{_libdir}/pkgconfig/spatialaudio.pc


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3.20200406gitd926a2e
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.1-1.20200406gitd926a2e
- Initial spec file
