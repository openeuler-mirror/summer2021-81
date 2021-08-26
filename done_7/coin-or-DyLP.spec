%global		module		DyLP

Name:		coin-or-%{module}
Summary:	Implementation of the dynamic simplex algorithm
Version:	1.10.4
Release:	5%{?dist}
License:	EPL-1.0
URL:		http://projects.coin-or.org/%{module}
Source0:	http://www.coin-or.org/download/pkgsource/%{module}/%{module}-%{version}.tgz
BuildRequires:	coin-or-Data-Netlib
BuildRequires:	coin-or-Osi-devel
BuildRequires:	coin-or-Osi-doc
BuildRequires:	doxygen
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	make

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Fix a sequence point error
Patch1:		%{name}-seqpoint.patch

%description
DyLP is an implementation of the dynamic simplex algorithm. Briefly, dynamic
simplex attempts to work with an active constraint system which is a subset
of the full constraint system. It alternates between primal and dual simplex
phases. Between simplex phases, it deactivates variables and constraints
which are not currently useful, and scans the full constraint system to
activate variables and constraints which have become useful.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Osi-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Osi-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n %{module}-%{version}

# Set the path to the error text message file
sed -i 's,\(DYLP_ERRMSGDIR=\).\$abs_source_dir.*,\1"%{_datadir}/coin/",' \
    configure

%build
%configure

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
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,dylp_addlibs.txt}
cp -a doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ -lm//' %{buildroot}%{_libdir}/pkgconfig/dylp.pc

# Install the error text message file
mkdir -p %{buildroot}%{_datadir}/coin
cp -p src/Dylp/dy_errmsgs.txt %{buildroot}%{_datadir}/coin

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test DYLP_ERRMSGDIR=$PWD/src/Dylp/

%ldconfig_scriptlets

%files
%license LICENSE
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/README
%{_libdir}/libDylp.so.1
%{_libdir}/libDylp.so.1.*
%{_libdir}/libOsiDylp.so.1
%{_libdir}/libOsiDylp.so.1.*
%{_datadir}/coin/

%files		devel
%{_includedir}/coin/*
%{_libdir}/libDylp.so
%{_libdir}/libOsiDylp.so
%{_libdir}/pkgconfig/dylp.pc
%{_libdir}/pkgconfig/osi-dylp.pc

%files		doc
%{_docdir}/%{name}/html
%{_docdir}/%{name}/dylp_doxy.tag

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 1.10.4-1
- Update to latest upstream release
- Change License from EPL to EPL-1.0
- Eliminate unnecessary BRs and Rs
- Install the error message text file
- Eliminate rpath from the library
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Filter out unnecessary Libs values from pkgconfig files
- Package doxygen tag file to enable cross-linking

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.10.3-7
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 15 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.10.3-1
- Update to latest upstream release
- Correct FTBFS in rawhide (#1307388)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.10.1-3
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.10.1-1
- Update to latest upstream release (#1089926)

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.9.4-4
- Rebuild to ensure using latest C++ abi changes.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.9.4-1
- Update to latest upstream release.

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.9.1-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.3-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.3-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.3-2
- Rename package to coin-or-DyLP.
- Do not package Thirdy party data or data without clean license.

* Thu Sep 27 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.3-1
- Initial coinor-DyLP spec.
