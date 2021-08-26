Name:		live555
Version:	2020.07.31
Release:	3%{?dist}
Summary:	Live555.com streaming libraries

License:	LGPLv2+
URL:		http://live555.com/liveMedia/
Source0:	%{url}/public/live.%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  openssl-devel

# Packages using live555 must Requires this:
#%%{?live555_version:Requires: live555%%{?_isa} = %%{live555_version}}


%description
This code forms a set of C++ libraries for multimedia streaming, 
using open standard protocols (RTP/RTCP, RTSP, SIP). These 
libraries - which can be compiled for Unix (including Linux and Mac OS X), 
Windows, and QNX (and other POSIX-compliant systems) - can be used 
to build streaming applications.
The libraries can also be used to stream, receive, and process MPEG, 
H.263+ or JPEG video, and several audio codecs. They can easily be 
extended to support additional (audio and/or video) codecs, and can 
also be used to build basic RTSP or SIP clients and servers, and have 
been used to add streaming support to existing media player applications.

%package	devel
Summary:	Development files for live555.com streaming libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This code forms a set of C++ libraries for multimedia streaming, 
using open standard protocols (RTP/RTCP, RTSP, SIP). These 
libraries - which can be compiled for Unix (including Linux and Mac OS X), 
Windows, and QNX (and other POSIX-compliant systems) - can be used 
to build streaming applications.
The libraries can also be used to stream, receive, and process MPEG, 
H.263+ or JPEG video, and several audio codecs. They can easily be 
extended to support additional (audio and/or video) codecs, and can 
also be used to build basic RTSP or SIP clients and servers, and have 
been used to add streaming support to existing media player applications.

%package	tools
Summary:	RTSP streaming tools using live555.com streaming libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	tools
This code forms a set of C++ libraries for multimedia streaming, 
using open standard protocols (RTP/RTCP, RTSP, SIP). These 
libraries - which can be compiled for Unix (including Linux and Mac OS X), 
Windows, and QNX (and other POSIX-compliant systems) - can be used 
to build streaming applications.
The libraries can also be used to stream, receive, and process MPEG, 
H.263+ or JPEG video, and several audio codecs. They can easily be 
extended to support additional (audio and/or video) codecs, and can 
also be used to build basic RTSP or SIP clients and servers, and have 
been used to add streaming support to existing media player applications.

This package contains the live555.com streaming server
(live555MediaServer), the example programs (openRTSP, playSIP, sapWatch,
vobStreamer) and a variety of test tools.


%prep
%setup -q -n live
sed -i -e "s|-O2|%{optflags}|" \
  config.linux-with-shared-libraries


%build
./genMakefiles %{_target_os}-with-shared-libraries
%make_build LDFLAGS="%{?__global_ldflags}"


%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}

#RPM Macros support
mkdir -p %{buildroot}%{rpmmacrodir}
cat > %{buildroot}%{rpmmacrodir}/macros.%{name} << EOF
# live555 RPM Macros
%live555_version	%{version}
EOF
touch -r COPYING %{buildroot}%{rpmmacrodir}/macros.%{name}

#Fix library dependency detection
chmod +x %{buildroot}%{_libdir}/*.so*


%ldconfig_scriptlets


%files
%license COPYING
%{_libdir}/libBasicUsageEnvironment.so.1*
%{_libdir}/libgroupsock.so.8*
%{_libdir}/libliveMedia.so.79*
%{_libdir}/libUsageEnvironment.so.3*

%files tools
%{_bindir}/*

%files devel
%doc README
%{rpmmacrodir}/macros.%{name}
%{_libdir}/libBasicUsageEnvironment.so
%{_libdir}/libgroupsock.so
%{_libdir}/libliveMedia.so
%{_libdir}/libUsageEnvironment.so
%{_includedir}/BasicUsageEnvironment/
%{_includedir}/groupsock/
%{_includedir}/liveMedia/
%{_includedir}/UsageEnvironment/


%changelog
* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2020.07.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2020.07.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Aug 01 2020 Leigh Scott <leigh123linux@gmail.com> - 2020.07.31-1
- Update to 2020.07.31

* Mon Apr 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 2020.04.12-1
- Update to 2020.04.12

* Thu Mar 05 2020 Nicolas Chauvet <kwizart@gmail.com> - 2020.02.25-1
- Update to 2020.02.25

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2019.07.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2019.07.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Aug 06 2019 Nicolas Chauvet <kwizart@gmail.com> - 2019.07.27-1
- Update to 2019.07.27

* Mon Jul 22 2019 Nicolas Chauvet <kwizart@gmail.com> - 2019.06.28-2
- Rebuilt

* Mon Jul 01 2019 Nicolas Chauvet <kwizart@gmail.com> - 2019.06.28-1
- Update to 2019.06.28

* Sat Apr 06 2019 Nicolas Chauvet <kwizart@gmail.com> - 2019.03.06-1
- Update to 2019.03.06

* Tue Mar 05 2019 Nicolas Chauvet <kwizart@gmail.com> - 2019.02.27-1
- Update to 2019.02.27

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2019.02.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Feb 26 2019 Nicolas Chauvet <kwizart@gmail.com> - 2019.02.03-1
- Update to 2019.02.03

* Sat Oct 20 2018 Nicolas Chauvet <kwizart@gmail.com> - 2018.10.17-1
- Update to 2018.10.17

* Fri Sep 21 2018 Nicolas Chauvet <kwizart@gmail.com> - 2018.09.18-1
- Update to 2018.09.18

* Tue Jul 24 2018 Nicolas Chauvet <kwizart@gmail.com> - 2018.07.07-1
- Update to 2018.07.07

* Thu May 10 2018 Alexandre Detiste <alexandre@detiste.be> - 2018.04.25-1
- Update to 2018.04.25

* Sun Mar 11 2018 Alexandre Detiste <alexandre@detiste.be> - 2018.02.28-1
- Update to 2018.02.28
- Remove workaround for 'xlocale.h' introduced in 2017.06.04-1,
  not needed anymore

* Sun Feb 25 2018 Alexandre Detiste <alexandre@detiste.be> - 2018.02.18-1
- Update to 2018.02.18

* Fri Feb 02 2018 Alexandre Detiste <alexandre@detiste.be> - 2018.01.29-1
- Update to 2018.01.29

* Fri Nov 24 2017 Alexandre Detiste <alexandre@detiste.be> - 2017.10.28-1
- Update to 2017.10.28

* Sun Sep 24 2017 Alexandre Detiste <alexandre@detiste.be> - 2017.09.12-1
- Update to 2017.09.12

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2017.07.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Alexandre Detiste <alexandre@detiste.be> - 2017.07.18-1
- Update to 2017.07.18

* Sun Jul 16 2017 Alexandre Detiste <alexandre@detiste.be> - 2017.06.04-1
- New release
- Use sed to out include of obsolete 'xlocale.h'
  https://bugzilla.redhat.com/show_bug.cgi?id=1464640

* Tue May 23 2017 Alexandre Detiste <alexandre@detiste.be> - 2017.04.26-1
- New release

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2017.01.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 20 2017 Nicolas Chauvet <kwizart@gmail.com> - 2017.01.26-1
- Update to 2017.01.26
- Switch to %%{rpmmacrodir}

* Mon Dec 12 2016 Nicolas Chauvet <kwizart@gmail.com> - 2016.11.28-1
- Update to 2016.11.28
- Switch to RPM based macros

* Fri Oct 28 2016 Nicolas Chauvet <kwizart@gmail.com> - 2016.10.21-1
- Update to 2016.10.21

* Tue Aug 16 2016 Leigh Scott <leigh123linux@googlemail.com> - 2016.07.19-3
- Add hardening flags to LDFLAGS

* Thu Jul 28 2016 Nicolas Chauvet <nicolas.chauvet@kwizart.fr> - 2016.07.19-2
- Update to 2016.07.19

* Sun May 22 2016 Nicolas Chauvet <kwizart@gmail.com> - 2016.05.20-1
- Update to 2016.05.20

* Sat Oct 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 2015.10.12-1
- Update to 2015.10.12

* Tue Oct 28 2014 Nicolas Chauvet <kwizart@gmail.com> - 2014.10.21-1
- Update to 2014.10.21

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 2014.02.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Feb 04 2014 Nicolas Chauvet <kwizart@gmail.com> - 2014.02.04-1
- Update to 2014.02.04

* Thu Nov 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 2013.11.26-1
- Update to 2013.11.26

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 2013.08.28-3
- Rebuilt

* Wed Aug 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 2013.08.28-2
- Update to 2013.08.28

* Sat May 25 2013 Nicolas Chauvet <kwizart@gmail.com> - 2013.04.30-1
- Update to 2013.04.30

* Wed Jan 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 2013.01.25-1
- Update to 2013.01.25

* Sun Jan 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 2013.01.19-1
- Update to 2013.01.19
- Spec file cleanup
- Drop upstreamed patches
- Drop static built, not usefull with standard options
- Rename the %%live555date macro to %%live555_version
  Dependencies must use the later instead.

* Thu Oct 18 2012 Nicolas Chauvet <kwizart@gmail.com> - 0-0.38.2012.10.18
- Update to 2012.10.18

* Tue May 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 0-0.37.2012.04.27
- Update to 2012.04.27

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0-0.36.2012.02.04
- Rebuilt for c++ ABI breakage

* Sun Feb 19 2012 Nicolas Chauvet <kwizart@gmail.com> - 0-0.35.2012.02.04
- Update to 2012.02.04

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0-0.34.2012.01.25
- Update to 2012.01.25
- Drop merged patch
- Back to LGPLv+2 license

* Mon Sep 19 2011 Nicolas Chauvet <kwizart@gmail.com> - 0-0.32.2011.09.02
- Update to 2011.09.02
- Reorder patches
- Add live-cloexec.patch and live-intptr.patch (rebased) from Rémi.

* Tue Jan 25 2011 Nicolas Chauvet <kwizart@gmail.com> - 0-0.30.2011.01.24
- Update to 2011.01.24
- Update live555 patches from Rémi.
- Use RPM macro to workaround inconsistent ABI dependency.

* Tue Jun 22 2010 Nicolas Chauvet <kwizart@gmail.com> - 0-0.28.2010.06.22
- Update to 2010.06.22

* Sat May  1 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0-0.27.2010.04.09
- Update to 2010.04.09
- Add patches from Rémi Denis-Courmont - provided as GPLv2+
- Distribute live555 as GPLv2+

* Thu Jan 28 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0-0.26.2010.01.22
- Update to 2010.01.22
  Fix multicast with openRTSP

* Sat Jan 16 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0-0.25.2010.01.16
- Update to 2010.01.16
- Update patch for shared library

* Mon Aug 17 2009 kwizart < kwizart at gmail.com > - 0-0.24.2009.07.28
- 2009.07.28
- Revert circle dependency (prefer undefined non_weak_symbol)
- Disable static libraries compiled with fpic.
- Use c++ to link - BZ #564

* Fri Apr 17 2009 kwizart < kwizart at gmail.com > - 0-0.23.2009.04.07
- Unified patches. (unrelevant fixes dropped).

* Tue Apr 07 2009 Dominik Mierzejewski <rpm[AT]greysector.net> - 0-0.22.2009.04.07
- 2009.04.07
- use new debian patchset

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0-0.21.2008.07.25
- rebuild for new F11 features

* Sun Aug 17 2008 Dominik Mierzejewski <rpm[AT]greysector.net> - 0-0.20.2008.07.25
- 2008.07.25
- devel-static -> static, per Fedora guidelines
- specfile whitespace cosmetics
- made tools depend on specific version until we have a stable ABI
- added proper obsoletes/provides to devel
- made -tools binaries installation independent of umask

* Mon May  5 2008 kwizart < kwizart at gmail.com > - 0-0.19.2008.04.03
- Rename package from live to live555 
  (live555-devel-static provides live-devel for compat)
- Enable shared build
- Split static pic and nopic into devel-static

* Sun Apr 06 2008 Dominik Mierzejewski <rpm[AT]greysector.net> - 0-0.18.2008.04.03
- 2008.04.03

* Sun Feb 24 2008 Dominik Mierzejewski <rpm[AT]greysector.net> - 0-0.17.2008.02.08
- 2008.02.08
- added tools subpackage

* Sat Dec 01 2007 Dominik Mierzejewski <rpm[AT]greysector.net> - 0-0.16.2007.11.18
- 2007.11.18
- fix CVE-2007-6036 (bug #1728)
- fix license tag
- store changelog.txt locally, because the one on the website is constantly updated

* Thu May 17 2007 Dominik Mierzejewski <rpm[AT]greysector.net> - 0-0.15.2007.04.24a
- 2007.04.24a
- use Debian patches

* Mon Sep 25 2006 Dams <anvil[AT]livna.org> - 0-0.13.2006.08.07%{?dist}
- Release bump

* Fri Aug 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 0-0.12.2006.08.07
- changelog.txt changed upstream :(

* Thu Aug 10 2006 Ville Skyttä <ville.skytta at iki.fi> - 0-0.11.2006.08.07
- 2006.08.07.
- Drop no longer needed live Obsoletes and Provides.
- Install into usual system locations, ship both PIC and non-PIC libs
  (from Debian).

* Thu Jun 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 0-0.11.2006.06.22
- 2006.06.22.
- Re-enable parallel make.

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- add another 0 for switch cvs -> release

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Thu Feb 23 2006 Ville Skyttä <ville.skytta at iki.fi> 0-0.lvn.11.2006.02.15
- Update to 2006.02.15.

* Mon Jan 16 2006 Adrian Reber <adrian@lisas.de> - 0-0.lvn.11.2006.01.05
- Updated to 2006.01.05
- Drop Epoch

* Tue Aug  9 2005 Ville Skyttä <ville.skytta at iki.fi> 0:0-0.lvn.10.2005.08.09
- 2005.08.09.
- Rename binary package to -devel.
- Ship changelog.txt.
- Clean up unused stuff from specfile.

* Tue Dec 28 2004 Dams <anvil[AT]livna.org> - 0:0-0.lvn.10.2004.12.23
- Updated to version 2004.12.23

* Fri Nov 12 2004 Dams <anvil[AT]livna.org> - 0:0-0.lvn.9.2004.11.11a
- Updated to version 2004.11.11a

* Thu May 20 2004 Dams <anvil[AT]livna.org> - 0:0-0.lvn.8.2004.05.19
- Added Source1:changelog.txt

* Thu May 20 2004 Dams <anvil[AT]livna.org> - 0:0-0.lvn.7.2004.05.19
- Updated version
- URL in Source0

* Sun Apr  4 2004 Dams <anvil[AT]livna.org> 0:0-0.lvn.6.2004.03.31
- Removed testprograms package

* Wed Mar 31 2004 Dams <anvil[AT]livna.org> 0:0-0.lvn.5.2004.03.31
- Updated version 2004-03-31

* Wed Jan  7 2004 Dams <anvil[AT]livna.org> 0:0-0.fdr.4.2003.11.25
- Patch from Marius to make makefile honor rpm optflags
- Removed URL in Source0

* Wed Jan  7 2004 Dams <anvil[AT]livna.org> 0:0-0.fdr.3.2003.11.25
- Removed all .o files

* Fri Dec 12 2003 Dams <anvil[AT]livna.org> 0:0-0.fdr.2.2003.11.25
- Snipped the devel pacakge. 

* Fri Dec 12 2003 Dams <anvil[AT]livna.org> 0:0-0.fdr.1.2003.11.25
- Version-Release respecting fedora.us guidelines
- Spec file cleanup. 

* Sat Nov 29 2003 Peter Backlund <peter dot backlund at home dot se> - 0:0.0.2003.11.25-0.fdr.1
- Added 0.0. to version, to allow for upgrade to 0.x/1.x release
 
* Sat Nov 29 2003 Peter Backlund <peter dot backlund at home dot se> - 0:2003.11.25-0.fdr.1
- New upstream release

* Sun Nov 16 2003 Peter Backlund <peter dot backlund at home dot se> - 0:2003.11.14-0.fdr.2
- Removed unnecessary BuildReq.
- Removed smp job macro.
- Replaced sed with perl.

* Fri Nov 14 2003 Peter Backlund <peter dot backlund at home dot se> - 0:2003.11.14-0.fdr.1
- Initial RPM release.
