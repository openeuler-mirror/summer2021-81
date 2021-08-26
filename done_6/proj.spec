%global proj_version 7.2.1
%global data_version 1.4

# The name is special so that rpmdev-bumpspec will bump this rather than adding .1 to the end
%global baserelease 2

# In order to avoid needing to keep incrementing the release version for the
# main package forever, we will just construct one for proj that is guaranteed
# to increment safely. Changing this can only be done during an update when the
# base proj version number is increasing.
%global data_release %{proj_version}.%{baserelease}%{?dist}

Name:           proj
# Also check whether there is a new proj-data release when upgrading!
Version:        %{proj_version}
Release:        %{baserelease}%{?dist}
Summary:        Cartographic projection software (PROJ)

License:        MIT
URL:            https://proj.org
Source0:        https://download.osgeo.org/%{name}/%{name}-%{version}.tar.gz
Source1:        https://download.osgeo.org/%{name}/%{name}-data-%{data_version}.tar.gz

# Ship a pkgconfig file
Patch0:         proj_pkgconfig.patch

BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel >= 1.8.0
BuildRequires:  make
BuildRequires:  libtiff-devel
BuildRequires:  sqlite-devel

Obsoletes:      proj-datumgrid < 1.8-6.3.2.6

%description
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions.


%package devel
Summary:        Development files for PROJ
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-static < 7.2.0

%description devel
This package contains libproj and the appropriate header files and man pages.


%package data-europe
Summary:        Compat package for old proj-datumgrid-europe
BuildArch:      noarch
Obsoletes:      proj-datumgrid-europe < 1.6-3
Provides:       deprecated()
Requires:       proj-data-at
Requires:       proj-data-be
Requires:       proj-data-ch
Requires:       proj-data-de
Requires:       proj-data-dk
Requires:       proj-data-es
Requires:       proj-data-eur
Requires:       proj-data-fi
Requires:       proj-data-fo
Requires:       proj-data-fr
Requires:       proj-data-is
Requires:       proj-data-nl
Requires:       proj-data-pt
Requires:       proj-data-se
Requires:       proj-data-sk
Requires:       proj-data-uk

%description data-europe
Compat package for old proj-datumgrid-europe.
Please do not depend on this package, it will get removed!

%files data-europe


%package data-north-america
Summary:        Compat package for old proj-datumgrid-north-america
BuildArch:      noarch
Obsoletes:      proj-datumgrid-north-america < 1.4-3
Provides:       deprecated()
Requires:       proj-data-ca
Requires:       proj-data-us

%description data-north-america
Compat package for old proj-datumgrid-north-america.
Please do not depend on this package, it will get removed!

%files data-north-america


%package data-oceania
Summary:        Compat package for old proj-datumgrid-oceania
BuildArch:      noarch
Obsoletes:      proj-datumgrid-oceania < 1.2-3
Provides:       deprecated()
Requires:       proj-data-au
Requires:       proj-data-nc
Requires:       proj-data-nz

%description data-oceania
Compat package for old proj-datumgrid-oceania.
Please do not depend on this package, it will get removed!

%files data-oceania


%package data-world
Summary:        Compat package for old proj-datumgrid-world
BuildArch:      noarch
Obsoletes:      proj-datumgrid-world < 1.0-5
Provides:       deprecated()
Requires:       proj-data-br
Requires:       proj-data-jp

%description data-world
Compat package for old proj-datumgrid-world.
Please do not depend on this package, it will get removed!

%files data-world



%define data_subpkg(c:n:e:s:) \
%define countrycode %{-c:%{-c*}}%{!-c:%{error:Country code not defined}} \
%define countryname %{-n:%{-n*}}%{!-n:%{error:Country name not defined}} \
%define extrafile %{-e:%{_datadir}/%{name}/%{-e*}} \
%define wildcard %{!-s:%{_datadir}/%{name}/%{countrycode}_*} \
\
%package data-%{countrycode}\
Summary:      %{countryname} datum grids for Proj\
BuildArch:    noarch\
# See README.DATA \
License:      CC-BY and MIT and BSD and Public Domain \
Supplements:  proj\
\
%description data-%{countrycode}\
%{countryname} datum grids for Proj.\
\
%files data-%{countrycode}\
%{wildcard}\
%{extrafile}


%data_subpkg -c at -n Austria
%data_subpkg -c au -n Australia
%data_subpkg -c be -n Belgium
%data_subpkg -c br -n Brasil
%data_subpkg -c ca -n Canada
%data_subpkg -c ch -n Switzerland
%data_subpkg -c de -n Germany
%data_subpkg -c dk -n Denmark -e DK
%data_subpkg -c es -n Spain
%data_subpkg -c eur -n %{quote:Nordic + Baltic} -e NKG
%data_subpkg -c fi -n Finland
%data_subpkg -c fo -n %{quote:Faroe Island} -e FO -s 1
%data_subpkg -c fr -n France
%data_subpkg -c is -n Island -e ISL
%data_subpkg -c jp -n Japan
%data_subpkg -c nc -n %{quote:New Caledonia}
%data_subpkg -c nl -n Netherlands
%data_subpkg -c nz -n %{quote:New Zealand}
%data_subpkg -c pt -n Portugal
%data_subpkg -c se -n Sweden
%data_subpkg -c sk -n Slovakia
%data_subpkg -c uk -n %{quote:United Kingdom}
%data_subpkg -c us -n %{quote:United States}


%prep
%autosetup -p1


%build
%cmake -DUSE_EXTERNAL_GTEST=ON
%cmake_build


%install
%cmake_install

# Install data
mkdir -p %{buildroot}%{_datadir}/%{name}
tar -xf %{SOURCE1} --directory %{buildroot}%{_datadir}/%{name}


%check
%ctest


%files
%license COPYING
%doc NEWS AUTHORS README.md
%{_bindir}/cct
%{_bindir}/cs2cs
%{_bindir}/geod
%{_bindir}/gie
%{_bindir}/proj
%{_bindir}/projinfo
%{_bindir}/projsync
%{_libdir}/libproj.so.21*
%{_libdir}/libproj.so.19
%{_mandir}/man1/*.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/CH
%{_datadir}/%{name}/GL27
%{_datadir}/%{name}/ITRF2000
%{_datadir}/%{name}/ITRF2008
%{_datadir}/%{name}/ITRF2014
%{_datadir}/%{name}/nad.lst
%{_datadir}/%{name}/nad27
%{_datadir}/%{name}/nad83
%{_datadir}/%{name}/other.extra
%{_datadir}/%{name}/proj.db
%{_datadir}/%{name}/proj.ini
%{_datadir}/%{name}/world
%{_datadir}/%{name}/README.DATA
%{_datadir}/%{name}/copyright_and_licenses.csv
%{_datadir}/%{name}/deformation_model.schema.json
%{_datadir}/%{name}/projjson.schema.json
%{_datadir}/%{name}/triangulation.schema.json

%files devel
%{_includedir}/*.h
%{_includedir}/proj/
%{_libdir}/libproj.so
%{_libdir}/cmake/proj/
%{_libdir}/cmake/proj4/
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Sandro Mani <manisandro@gmail.com> - 7.2.1-1
- Update to 7.2.1

* Thu Nov 12 2020 Sandro Mani <manisandro@gmail.com> - 7.2.0-2
- Add Provides: deprecated() to compat packages

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 7.2.0-1
- Update to 7.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Markus Neteler <neteler@mundialis.de> - 6.3.2-2
- disable gtest external on EPEL8 due to compilation error

* Sat May 02 2020 Sandro Mani <manisandro@gmail.com> - 6.3.2-1
- Update to 6.3.2

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 6.3.1-3
- Fix datumgrid require

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 6.3.1-2
- Fix proj-datumgrid release missing %%{?dist}

* Wed Feb 19 2020 Sandro Mani <manisandro@gmail.com> - 6.3.1-1
- Update to 6.3.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 1 2019 Devrim Gündüz <devrim@gunduz.org> - 6.2.0-1
- Update to 6.2.0
- Applied https://src.fedoraproject.org/rpms/proj/pull-request/6 by
  Orion Poplawski.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Dan Horák <dan[at]danny.cz> - 5.2.0-4
- fix condition in cmake config

* Tue Apr 16 2019 Dan Horák <dan[at]danny.cz> - 5.2.0-3
- install cmake config

* Sat Apr 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.2.0-2
- Rename proj-nad subpackage as proj-datumgrid
- Fold proj-epsg package into main one
- Enable full test suite during build
- Various spec file cleanups

* Mon Feb 04 2019 Devrim Gündüz <devrim@gunduz.org> - 5.2.0-1
- Update to 5.2.0
- Update to new datumgrid (1.8)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Devrim Gündüz <devrim@gunduz.org> 4.9.3-1
- Update to 4.9.3
- Update to new datumgrid (1.6)
- Fix rpmlint warnings
- Cosmetic cleanup  in spec file.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 4 2016 Devrim Gündüz <devrim@gunduz.org> 4.9.2-1
- Update to 4.9.2, per bz # 1294604
- Update URLs.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.9.1-2
- track soname so bumps are not a suprise
- -devel: include .pc file here (left copy in -nad too)
- -static: Requires: -devel

* Wed Mar 11 2015 Devrim Gündüz <devrim@gunduz.org> 4.9.1-1
- Update to 4.9.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Devrim Gündüz <devrim@gunduz.org> 4.8.0-3
- Install projects.h manually, per #830496.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Devrim Gündüz <devrim@gunduz.org> 4.8.0-1
- Update to 4.8.0, per bz #814851

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 18 2010 Balint Cristian <cristian.balint@gmail.com> - 4.7.0-3
- fix for bz#562671

* Thu Mar 18 2010 Balint Cristian <cristian.balint@gmail.com> - 4.7.0-2
- fix for bz#556091

* Fri Dec 4 2009 Devrim Gündüz <devrim@gunduz.org> 4.7.0-1
- Update to 4.7.0
- Update to new datumgrid (1.5)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 05 2008 Balint Cristian <rezso@rdsor.ro> - 4.6.1-1
- new stable upstream
- new nad datumgrids
- drop debian license patch
- change homepage URLs

* Sun Apr 20 2008 Balint Cristian <rezso@rdsor.ro> - 4.6.0-1
- new branch

* Thu Mar 27 2008 Balint Cristian <rezso@rdsor.ro> - 4.5.0-4
- BuildRequire: libtool

* Thu Mar 27 2008 Balint Cristian <rezso@rdsor.ro> - 4.5.0-3
- enable EPSG dataset to be packed GRASS really needs it
- no more license issue over epsg dataset, proj didnt altered
  EPSG dataset in any way, so its fully EPSG license compliant
- add support for tests during buildtime
- disable hardcoded r-path from libs
- fix shebag for nad scripts

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.5.0-2
- Autorebuild for GCC 4.3

* Tue Jan   2 2007 Shawn McCann <mccann0011@hotmail.com> - 4.5.0-1
- Updated to proj-4.5.0 and datumgrid-1.3

* Sat Sep  16 2006 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-4
- Rebuild for Fedora Extras 6

* Sat Mar  4 2006 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-3
- Rebuild for Fedora Extras 5

* Sat Mar  4 2006 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-2
- Rebuild for Fedora Extras 5

* Thu Jul  7 2005 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-1
- Updated to proj-4.4.9 and to fix bugzilla reports 150013 and 161726. Patch2 can be removed once this package is upgraded to the next release of the source.

* Sun May 22 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 4.4.8-6
- rebuilt

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 4.4.8-5
- rebuilt

* Wed Dec 29 2004 David Kaplan <dmk@erizo.ucdavis.edu> - 0:4.4.8-4
- Added testvarious to nad distribution

* Wed Dec 29 2004 David Kaplan <dmk@erizo.ucdavis.edu> - 0:4.4.8-0.fdr.3
- Added patch for test scripts so that they will work in installed rpm

* Wed Dec 29 2004 David Kaplan <dmk@erizo.ucdavis.edu> - 0:4.4.8-0.fdr.2
- Fixed permissions on nad27 and nad83
- Included test27 and test83 in the nad rpm and made them executable

* Fri Aug 13 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:4.4.8-0.fdr.1
- Updated to version 4.4.8 of library.
- Changed license file so that it agrees with Debian version.
- Updated web addresses of packages.

* Wed Aug 11 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:4.4.7-0.fdr.3
- Removed the "Requires(post,postun)"

* Tue Dec 30 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:4.4.7-0.fdr.2
- proj-nad now owns %%{_datadir}/%%{name}

* Wed Oct 29 2003 Steve Arnold <sarnold@arnolds.dhs.org>
- Basically re-wrote previous spec file from scratch so as
- to comply with both Fedora and RedHat 9 packaging guidelines.
- Split files into proj, proj-devel, and proj-nad (additional grids)
- and adjusted the EXE path in the test scripts.
