%define name	simsam
%define version	0.1.8
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Simple sampler for MIDI
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch0:		simsam-0.1.8-fix-gcc4.3.patch
Patch1:		simsam-0.1.8-fix-str-fmt.patch
URL:		https://simsam.sourceforge.net/
License:	GPLv2
Group:		Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pkgconfig qt3-devel
BuildRequires:	jackit-devel libsamplerate-devel libsndfile-devel alsa-lib-devel

%description
Simsam is a simple MIDI sample playback program. You can use it to play drum
samples and loops from a MIDI keyboard or sequencer.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
PATH="/usr/lib/qt3/bin:$PATH" ; export PATH ;
%configure2_5x --with-Qt-bin-dir=%_prefix/lib/qt3/bin --with-Qt-lib-dir=%{_libdir}
%make
										
%install
rm -rf %{buildroot}
%makeinstall

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=SimSam
Comment=Simple Sampler
Categories=Audio;
EOF

%clean
rm -rf %{buildroot}

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

