%global commit 09e8db1c1681704d7c21d5dda77c0623c5102705
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20210107

Summary: GNOME version of a tetris game playable on the net
Name: gtetrinet
Version: 0.7.11
Release: 20.%{gitdate}.git%{shortcommit}%{?dist}
License: GPLv2+
Group: Amusements/Games
URL: http://gtetrinet.sourceforge.net/
Source0: https://github.com/tatankat/gtetrinet/archive/%{commit}/gtetrinet-%{shortcommit}.tar.gz
Source1: tetrinet.txt
Source2: http://www.mavit.pwp.blueyonder.co.uk/mmr-sounds-1.0.tar.gz
Source3: %{name}.appdata.xml

BuildRequires: gcc
BuildRequires: make
BuildRequires: gtk3-devel
BuildRequires: glib2-devel >= 2.32.0
#BuildRequires: libgnome-devel >= 2.0.0
#BuildRequires: libgnomeui-devel >= 2.0.0
BuildRequires: libcanberra-devel
BuildRequires: autoconf automake libtool gettext-devel
BuildREquires: popt-devel
#BuildRequires: perl(XML::Parser)

Recommends: tetrinetx

%description
GTetrinet is a client program for the popular Tetrinet game, a multiplayer
tetris game that is played over the internet. (If you don't know what Tetrinet
is, check out tetrinet.org)


%prep
%autosetup -p1 -n gtetrinet-%{commit}

%build
autoreconf --install --verbose
%configure
%make_build


%install
%make_install

%find_lang %{name} --with-gnome
%{__cp} -ap %{SOURCE1} .
%{__tar} -xzvf %{SOURCE2} -C %{buildroot}%{_datadir}/gtetrinet/themes/
install -m 0644 -D %{SOURCE3} %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README.md tetrinet.txt
%license COPYING
%{_bindir}/gtetrinet
%{_datadir}/applications/gtetrinet.desktop
%{_datadir}/gtetrinet/
%{_datadir}/pixmaps/gtetrinet/
%{_datadir}/pixmaps/gtetrinet.png
%{_mandir}/man6/gtetrinet.6*
%{_datadir}/glib-2.0/schemas/*.xml
%{_metainfodir}/%{name}.appdata.xml


%changelog
* Thu May 20 2021 Sérgio Basto <sergio@serjux.com> - 0.7.11-20
- Change to fork of user tatankat which have gtk3 support

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 01 2020 Sérgio Basto <sergio@serjux.com> - 0.7.11-17
- Update gtetrinet.spec and his patches
- Add appdata file, copied from
  https://github.com/sanjayankur31/rpmfusion-appdata

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

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

