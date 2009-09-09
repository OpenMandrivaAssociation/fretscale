Summary:	Calculates fret distances for stringed musical instruments
Name:		fretscale
Version:	2.0
Release:	%mkrel 7
Group:		Sound
License:	GPL
# this url is dead...
URL:            http://members.safepages.net/gurensan/
Source0:	fretscale-%{version}.tar.bz2
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	X11-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
fretscale finds fret distances from the nut for stringed musical
instruments based on scale length/# frets/decimal accuracy. It can
output with/without a heading and with/without the remaining scale
distance after each fret. 

%prep

%setup -q

%build
export QTDIR=%{_prefix}/lib/qt3
export KDEDIR=%{_prefix}

qmake

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 bin/fretscale %{buildroot}%{_bindir}/


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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


