#global pre_release .pre1

Name:		libva
Version:	2.11.0
Release:	1%{?dist}
Summary:	Video Acceleration (VA) API for Linux
License:	MIT
URL:		https://github.com/intel/libva
Source0:	%{url}/archive/%{version}%{?pre_release}/%{name}-%{version}%{?pre_release}.tar.gz

BuildRequires:	libtool

BuildRequires:	libudev-devel
BuildRequires:	libXext-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libdrm-devel
BuildRequires:	libpciaccess-devel
BuildRequires:	mesa-libEGL-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	mesa-libGLES-devel
%{!?_without_wayland:
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(wayland-client) >= 1
BuildRequires:  pkgconfig(wayland-scanner) >= 1
BuildRequires: make
}
# owns the %%{_libdir}/dri directory
Requires:	mesa-dri-filesystem

%description
Libva is a library providing the VA API video acceleration API.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}%{?pre_release}
autoreconf -vif

%build
%configure --disable-static \
  --enable-glx \
%{?_without_wayland:--disable-wayland}

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install INSTALL="install -p"
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%ldconfig_scriptlets

%files
%doc NEWS
%license COPYING
%ghost %{_sysconfdir}/libva.conf
%{_libdir}/libva*.so.*

%files devel
%{_includedir}/va
%{_libdir}/libva*.so
%{_libdir}/pkgconfig/libva*.pc

%changelog
* Wed Mar 24 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.11.0-1
- Update to 2.11.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Sun Sep 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.9.0-1
- Update to 2.9.0

* Tue Sep 01 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.9.0-0.1.pre1
- Update to 2.9.0.pre1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.8.0-1
- Update to 2.8.0

* Mon Apr 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.7.1-1
- Update to 2.7.1

* Tue Apr 14 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.7.0-4
- Backport upstream fix for Intel Iris Driver (https://github.com/intel/libva/pull/406)

* Fri Apr 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.7.0-3
- Drop previous patch

* Sat Apr 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.7.0-2
- Update mapping for iris

* Thu Apr 02 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.7.0-1
- Update to 2.7.0

* Wed Mar 18 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.7.0-0.1.pre1
- Update to 2.7.0.pre1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.6.1-1
- Update to 2.6.1

* Mon Dec 30 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.6.0-1
- Update to 2.6.0 release

* Fri Dec 20 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.6.0-0.2
- Fixed missed slice parameter

* Sun Sep 22 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.6.0-0.1
- Update to 2.6.0-pre1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.5.0-1
- Update to 2.5.0

* Mon Apr 08 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Fri Oct 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Sat Jun 02 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.1-0.1.pre1
- Update to 2.1.1.pre1-20180601

* Mon Mar 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-2
- Switch to github.com/intel URL

* Mon Feb 12 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-2
- Switch to %%ldconfig_scriptlets

* Tue Oct 24 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Thu Aug 24 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.3-4
- Owns /etc/libva.conf and add NEWS in doc

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.3-1
- Update to 1.8.3
- Remove dummy driver

* Tue May 23 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Mon Apr 10 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Fri Mar 31 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.0-1
- Update to 1.8.0
- Switch upstream URL to 01.org and github
- Split libva-utils into it's own package
- Clean-up groups

* Wed Feb 15 2017 Hans de Goede <hdegoede@redhat.com> - 1.7.3-3
- Fix libva not working when using with libglvnd + wayland (rhbz#1422151)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 10 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.7.3-1
- Update to 1.7.3

* Mon Sep 05 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.7.2-1
- Update to 1.7.2

* Tue Jun 21 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Sun Mar 20 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Mon Sep 14 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.6.1-1
- Update to 1.6.1

* Mon Aug 03 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Sat Oct 25 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Wed Oct  8 2014 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 1.4.0-1
- Update to 1.4.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Elad Alfassa <elad@fedoraproject.org> - 1.3.1-3
- Apply upstream patch to fix a firefox crash (rhbz #1105890)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Tue Apr 08 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1
- Update to 1.3.0
- Enable wayland by default

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2.1-1
- Update to 1.2.1
- Add mpeg2vaenc

* Wed Jun 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-1
- Update to 1.2.0
- Exclude mpeg2enc for now - namespace clash

* Fri Apr 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.1-2
- Switch Requires to mesa-dri-filesystem

* Wed Mar 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-5
- Drop wayland support - Lead to suspicious crash
  to reintroduce later using alternates build for vainfo and libs.

* Thu Nov 15 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-4
- Fix condition rhbz#877059

* Sat Oct 06 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-3
- Update to official 1.1.0 release
- Enable Wayland support on f18 - add subpackage
- Clean spec file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-1
- Update to 1.1.0 - VA-API version 0.33.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 03 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.15-1
- Update to 1.0.15
- Back to vanilla upstream sources - no backend are provided anymore

* Sun Aug 07 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.14-1
- Update to 1.0.14

* Fri Jun 10 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.13-2
- Add versioned requirement between main/utils

* Wed Jun 08 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.13-1
- Update to 1.0.13

* Fri Apr 08 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.12-1
- Update to 1.0.12

* Mon Feb 21 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.10-1
- Update to 1.0.10

* Tue Jan 25 2011 Adam Williamson <awilliam@redhat.com> - 1.0.8-1
- bump to new version
- fix modded tarball to actually not have i965 dir
- merge with the other spec I seem to have lying around somewhere

* Wed Nov 24 2010 Adam Williamson <awilliam@redhat.com> - 1.0.6-1
- switch to upstream from sds branch (sds now isn't carrying any very
  interesting changes according to gwenole)
- pull in the dont-install-test-programs patch from sds
- split out libva-utils again for multilib purposes
- drop -devel package obsolete/provides itself too

* Tue Nov 23 2010 Adam Williamson <awilliam@redhat.com> - 0.31.1-3.sds4
- drop obsoletes and provides of itself (hangover from freeworld)

* Tue Nov 23 2010 Adam Williamson <awilliam@redhat.com> - 0.31.1-2.sds4
- fix the tarball to actually remove the i965 code (duh)

* Thu Oct 7 2010 Adam Williamson <awilliam@redhat.com> - 0.31.1-1.sds4
- initial package (based on package from elsewhere by myself and Nic
  Chauvet with i965 driver removed)
