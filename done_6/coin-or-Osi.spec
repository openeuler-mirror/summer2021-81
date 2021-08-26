%global		module		Osi

Name:		coin-or-%{module}
Summary:	COIN-OR Open Solver Interface Library
Version:	0.108.6
Release:	3%{?dist}
License:	EPL-1.0
URL:		https://github.com/coin-or/%{module}
Source0:	%{url}/archive/releases/%{version}/%{module}-%{version}.tar.gz
# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch
# Fix build with glpk > 4.48
Patch1:		%{name}-glpk.patch

BuildRequires:	coin-or-CoinUtils-doc
BuildRequires:	coin-or-Data-Netlib
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	glpk-devel
BuildRequires:	make
BuildRequires:	pkgconfig(coinutils)

%description
The COIN-OR Open Solver Interface Library is a collection of solver
interfaces (SIs) that provide a common interface --- the OSI API --- for all
the supported solvers.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-CoinUtils-devel%{?_isa}
Requires:	glpk-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-CoinUtils-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n %{module}-releases-%{version}

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @OSILIB_PCLIBS@/\nLibs.private:&/' Osi/osi.pc.in

%build
%configure --with-glpk-incdir=%{_includedir} --with-glpk-lib=-lglpk

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all doxydoc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,osi_addlibs.txt}
cp -a doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%ldconfig_scriptlets

%files
%license LICENSE
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/README
%{_libdir}/libOsi.so.1
%{_libdir}/libOsi.so.1.*
%{_libdir}/libOsiCommonTests.so.1
%{_libdir}/libOsiCommonTests.so.1.*
%{_libdir}/libOsiGlpk.so.1
%{_libdir}/libOsiGlpk.so.1.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libOsi.so
%{_libdir}/libOsiCommonTests.so
%{_libdir}/libOsiGlpk.so
%{_libdir}/pkgconfig/osi.pc
%{_libdir}/pkgconfig/osi-glpk.pc
%{_libdir}/pkgconfig/osi-unittests.pc

%files		doc
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/osi_doxy.tag

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.108.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.108.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 2020 Jerry James <loganjerry@gmail.com> - 0.108.6-1
- Version 0.108.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.108.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Jerry James <loganjerry@gmail.com> - 0.108.5-1
- Update to latest upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.108.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 0.108.4-1
- Update to latest upstream release (bz 1461042)
- Update project URL
- Change License from EPL to EPL-1.0
- Eliminate unnecessary BRs and Rs
- Add -glpk patch to fix build with glpk > 4.48
- Eliminate rpath from the library
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Package doxygen tag file to enable cross-linking

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.107.8-8
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 0.107.8-3
- Rebuild for glpk 4.61

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 11 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.107.8-1
- Update to latest upstream release (#1308287)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.107.6-1
- Update to latest upstream release (#1257932)

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.107.4-3
- Full rebuild or coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.107.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.107.4-1
- Update to latest upstream release (#1199722)

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.107.2-3
- Rebuild to ensure using latest C++ abi changes.

* Sat Feb 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.107.2-2
- Rebuild.

* Mon Feb  9 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.107.2-1
- Update to latest upstream release (#1190730).

* Mon Feb  9 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.107.0-3
- Rebuild with latest bugfixes release coin-or-CoinUtils-2.10.3

* Sun Feb 08 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.107.0-2
- Rebuild with updated coin-or-CoinUtils.

* Sat Feb 07 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.107.0-1
- Update to latest upstream release (#1159476).

* Sun Aug 31 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.106.9-2
- Rebuild to ensure packages are built in proper order.

* Sat Aug 30 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.106.9-1
- Update to latest upstream release (#1133197#c3).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.106.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.106.7-1
- Update to latest upstream release (#1089928).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.106.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.106.2-3
- Use proper _smp_flags macro (#894586#c6).

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.106.2-2
- Correct missing bzip2 build requires (#894586#c4).
- Use unversioned docdir (#894586#c4).

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.106.2-1
- Update to latest upstream release.

* Wed May 8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.105.7-2
- Split documentation in a new subpackage.
- Switch to the new upstream tarballs without bundled dependencies.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.105.7-1
- Update to latest upstream release.

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.105.5-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.105.5-2
- Rename package to coin-or-Osi.
- Do not package Thirdy party data or data without clean license.

* Wed Sep 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.105.5-1
- Initial coinor-Osi spec.
