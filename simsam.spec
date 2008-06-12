%define name	simsam
%define version	0.1.7
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Simple sampler for MIDI
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch:		simsam-0.1.7-gcc3_4.patch.bz2
URL:		http://simsam.sourceforge.net/
License:	GPL
Group:		Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pkgconfig qt3-devel
BuildRequires:	jackit-devel libsamplerate-devel libsndfile-devel alsa-lib-devel

%description
Simsam is a simple MIDI sample playback program. You can use it to play drum
samples and loops from a MIDI keyboard or sequencer.

%prep
%setup -q
%patch -p1

%build
%configure2_5x --with-Qt-bin-dir=%_prefix/lib/qt3/bin --with-Qt-lib-dir=%_prefix/lib/qt3/%_lib
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=SimSam
Comment=Simple Sampler
Categories=Audio;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%name.desktop

