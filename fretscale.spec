Summary:	Calculates fret distances for stringed musical instruments
Name:		fretscale
Version:	2.0
Release:	%mkrel 10
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


