Summary:	Calculates fret distances for stringed musical instruments
Name:		fretscale
Version:	2.0
Release:	11
Group:		Sound
License:	GPLv2+
# this url is dead...
#URL:            http://members.safepages.net/gurensan/
Source0:	fretscale-%{version}.tar.bz2
BuildRequires:	qt3-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
fretscale finds fret distances from the nut for stringed musical
instruments based on scale length/# frets/decimal accuracy. It can
output with/without a heading and with/without the remaining scale
distance after each fret. 

%prep
%setup -q

%build
%qmake_qt3
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 bin/fretscale %{buildroot}%{_bindir}/


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=FretScale
Comment=Calculates fret distances for stringed musical instruments
Exec=%{_bindir}/%{name} 
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;Recorder;
EOF


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,755)
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop




%changelog
* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 2.0-10mdv2011.0
+ Revision: 635430
- simplify BR

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-9mdv2011.0
+ Revision: 610773
- rebuild

* Tue Dec 08 2009 Jérôme Brenier <incubusss@mandriva.org> 2.0-8mdv2010.1
+ Revision: 475184
- BuildRequires qt3-devel instead of kdelibs-devel (not needed)
- use the %%qmake_qt3 macro
- fix license tag
- comment URL (url dead)
- $RPM_BUILD_ROOT -> %%{buildroot}

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.0-4mdv2008.1
+ Revision: 136423
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - do not harcode icon extension
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Mar 16 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2.0-4mdv2007.1
+ Revision: 145092
- Add XDG menu
- Import fretscale

* Tue Jun 27 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0-4mdv2007.0
- rebuild

* Wed May 11 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0-3mdk
- lib64 fixes

* Sat Jun 05 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0-2mdk
- rebuilt against new deps and with gcc v3.4.x

