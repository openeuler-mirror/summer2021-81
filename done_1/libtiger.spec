Name:           libtiger
Version:        0.3.4
Release:        21%{?dist}
Summary:        Rendering library for Kate streams using Pango and Cairo

License:        LGPLv2+
URL:            http://libtiger.googlecode.com
Source0:        http://libtiger.googlecode.com/files/libtiger-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libkate-devel >= 0.2.7
BuildRequires:  pango-devel
%ifarch %{ix86} x86_64 ppc ppc64 s390x %{arm}
BuildRequires:  valgrind
%endif
BuildRequires:  doxygen


%description
Libtiger is a rendering library for Kate streams using Pango and Cairo.
More information about Kate streams may be found at 
http://wiki.xiph.org/index.php/OggKate


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pango-devel
Requires:       libkate-devel >= 0.2.7

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains Documentation for %{name}.



%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT __doc
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Fix timestramps change
touch -r include/tiger/tiger.h.in $RPM_BUILD_ROOT%{_includedir}/tiger/tiger.h

# Move docdir
mv $RPM_BUILD_ROOT%{_docdir}/%{name} __doc


%ldconfig_scriptlets


%files
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.*

%files devel
%{_includedir}/tiger/
%{_libdir}/*.so
%{_libdir}/pkgconfig/tiger.pc

%files doc
%doc examples __doc/html


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-7
- Set the current valgrind arches

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr  1 2011 Dan Horák <dan[at]danny.cz> - 0.3.4-2
- valgrind exists only on selected architectures

* Sun Mar 27 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-1
- Update to 0.3.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  5 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.3.3-3
- Only pick __doc/html in the doc subpackage.

* Tue Jan 26 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.3.3-2
- Split doc subpackage

* Thu Jul  2 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3

* Fri Nov 28 2008 kwizart < kwizart at gmail.com > - 0.3.2-1
- Update to 0.3.2

* Thu Sep  4 2008 kwizart < kwizart at gmail.com > - 0.1.1-1
- Initial spec file

