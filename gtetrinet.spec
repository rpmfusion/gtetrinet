Summary: GNOME version of a tetris game playable on the net
Name: gtetrinet
Version: 0.7.11
Release: 15%{?dist}
License: GPLv2+
Group: Amusements/Games
URL: http://gtetrinet.sourceforge.net/
Source0: https://github.com/GNOME/gtetrinet/archive/GTETRINET_0_7_11/gtetrinet-GTETRINET_0_7_11.tar.gz
Source1: tetrinet.txt
Source2: http://www.mavit.pwp.blueyonder.co.uk/mmr-sounds-1.0.tar.gz
Patch1: GTETRINET_0_7_11...master.diff
#Patch2: master...stump:master.diff
Patch2: master...stump:12cec675f4354d585ef754813b79695db30a8b1e.diff
Patch3: gtetrinet-intl.patch

BuildRequires: gtk2-devel >= 2.18.0
BuildRequires: glib2-devel >= 2.32.0
BuildRequires: libgnome-devel >= 2.0.0
BuildRequires: libgnomeui-devel >= 2.0.0
#BuildRequires: esound-devel
BuildRequires: libcanberra-devel
BuildRequires: autoconf automake libtool gettext-devel intltool
BuildRequires: perl(XML::Parser)

%description
GTetrinet is a client program for the popular Tetrinet game, a multiplayer
tetris game that is played over the internet. (If you don't know what Tetrinet
is, check out tetrinet.org)


%prep
%autosetup -p1 -n gtetrinet-GTETRINET_0_7_11

%build
mkdir m4
autoreconf -i 
intltoolize
%configure --disable-dependency-tracking --enable-ipv6
%make_build


%install
%make_install GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 \
    gamesdir=%{_bindir}
%find_lang %{name}
%{__cp} -ap %{SOURCE1} .
%{__tar} -xzvf %{SOURCE2} -C %{buildroot}%{_datadir}/gtetrinet/themes/


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README tetrinet.txt
%license COPYING
%config %{_sysconfdir}/gconf/schemas/gtetrinet.schemas
%{_bindir}/gtetrinet
%{_datadir}/applications/gtetrinet.desktop
%{_datadir}/gtetrinet/
%{_datadir}/pixmaps/gtetrinet/
%{_datadir}/pixmaps/gtetrinet.png
%{_mandir}/man6/gtetrinet.6*


%changelog
* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.7.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.7.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.7.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 18 2016 Sérgio Basto <sergio@serjux.com> - 0.7.11-9
- Clean spec, add license tag
- Switch to github sources 
- Add patch to update to git master 
- Add patch from fork of user stump, but removed last 3 commits, they break menu
  translations.
- Use autoreconf and libtoolize

* Sun May 10 2015 Sérgio Basto <sergio@serjux.com> - 0.7.11-8
- Fix FTBFS on F22, rfbz #3632

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.7.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.7.11-6
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.7.11-4
- rebuild for new F11 features

* Sun Dec 28 2008 Matthias Saou <http://freshrpms.net/> 0.7.11-3
- Minor spec file cleanups.
- Move binary back to _bindir (#279).

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.7.11-2
- rebuild for RPM Fusion

* Sun Dec 10 2006 Dag Wieers <dag@wieers.com> - 0.7.11-1
- Updated to release 0.7.11.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.7.9-2
- Release bump to drop the disttag number in FC5 build.

* Thu May 26 2005 Matthias Saou <http://freshrpms.net/> 0.7.9-1
- Update to 0.7.9.

* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 0.7.8-1
- Update to 0.7.8.

* Wed May  5 2004 Matthias Saou <http://freshrpms.net/> 0.7.7-1
- Update to 0.7.7.
- Minor spec updates (more macros), added perl(XML::Parser) build dep.
- Updated download URL (dl.sf.net -> ftp.gnome.org).

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.7.5-1
- Update to 0.7.5.
- Rebuild for Fedora Core 1.

* Fri Aug 29 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.7.4.
- Update to reflect the new style desktop entry.

* Wed Jun 25 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.7.3.

* Wed Jun 11 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.7.2.

* Tue Apr 15 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.7.1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Mar 18 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.7.0.

* Tue Feb 11 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.6.2.

* Wed Feb  5 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.6.0.

* Sat Jan 11 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.5.2.

* Tue Jan  7 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.5.1.

* Mon Oct 21 2002 Matthias Saou <http://freshrpms.net/>
- Updated to 0.4.3.
- Spec file cleanup, now use %%find_lang.
- New menu entry.

* Sun Oct 20 2002 Peter Oliver <p.d.oliver@mavit.freeserve.co.uk>
- Updated to 0.4.2.
- Added my preferred theme to the package.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Wed Apr 25 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and rebuilt for Red Hat 7.1.
- I think this was one of my first RPMs ;-)

* Mon Jul 03 2000 Matthias Saou <http://freshrpms.net/>
  [gtetrinet-0.4.1-1]
- Updated to version 0.4.1
- Cleaned up the build process
- Added the original tetrinet.txt help file

* Mon Jan 24 2000       <jasper@stack.nl>
  - Fixed typo in spec file <Shane Smit>

* Tue Dec 21 1999       <jasper@stack.nl>
  - First RPM release

