Name:           libudfread
Version:        1.1.2
Release:        1%{?dist}
Summary:        UDF reader library
License:        LGPLv2+
URL:            https://code.videolan.org/videolan/libudfread
Source0:        https://code.videolan.org/videolan/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires: make


%description
This library allows reading UDF filesystems, like raw devices and image files.
The library is created and maintained by VideoLAN Project and is used by
projects like VLC and Kodi.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
autoreconf -vif
%configure --disable-static
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc ChangeLog
%license COPYING
%{_libdir}/libudfread.so.0*

%files devel
%{_includedir}/udfread/
%{_libdir}/libudfread.so
%{_libdir}/pkgconfig/libudfread.pc


%changelog
* Tue Apr 06 2021 Xavier Bachelot <xavier@bachelot.org> 1.1.2-1
- Update to 1.1.2 (RHBZ#1946205)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Xavier Bachelot <xavier@bachelot.org> 1.1.1-1
- Update to 1.1.1 (RHBZ#1893436)

* Thu Sep 03 2020 Xavier Bachelot <xavier@bachelot.org> 1.1.0-2
- Don't glob _includedir
- Patch obsolete m4 macro

* Thu Aug 13 2020 Xavier Bachelot <xavier@bachelot.org> 1.1.0-1
- Initial package
