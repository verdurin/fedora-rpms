Name:		yoshimi
Version:	1.0.0
Release:	1%{?dist}
Summary:	Rewrite of ZynAddSubFx aiming for better JACK support

Group:		Applications/Multimedia
License:	GPLv2+
URL:		http://sourceforge.net/projects/%{name}
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
#Source1:	%{name}.desktop
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	cmake 
BuildRequires:	zlib-devel 
BuildRequires:	fontconfig-devel
BuildRequires:	fltk-devel 
BuildRequires:	fltk-fluid 
BuildRequires:	fftw3-devel
BuildRequires:	mxml-devel 
BuildRequires:	alsa-lib-devel 
BuildRequires:	libsndfile-devel
BuildRequires:	desktop-file-utils 
BuildRequires:	boost-devel

%description

Yoshimi is a rewrite of ZynAddSubFx to improve its compatibility with
the Jack Audio Connection Kit.

ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

%prep
%setup -q


%build
cd src
%cmake .
make VERBOSE=1 %{?_smp_mflags}


%install
rm -rf %{buildroot}

cd src
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 644 ../desktop/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

#Remove superfluous file
rm %{buildroot}%{_datadir}/%{name}/banks/chip/.bankdir

# Fix directory permissions without affecting patch files
chmod 755  %{buildroot}%{_datadir}/%{name}/banks
chmod 755  %{buildroot}%{_datadir}/%{name}/banks/*
chmod 755 %{buildroot}%{_datadir}/%{name}/presets
chmod 755 %{buildroot}%{_datadir}/%{name}/presets/*


%clean
rm -rf %{buildroot}

%post
update-desktop-database -q
touch --no-create %{_datadir}/icons/hicolor/scalable/apps/ >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor/scalable/apps >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor/scalable/apps >&/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor.scalable/apps &>/dev/null || :

%files
%defattr(-,root,root,-)
%doc %{version}.notes COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/banks/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png
%{_datadir}/%{name}/presets/

%changelog
* Sun Jul 29 2012  <bloch@verdurin.com> - 1.0.0-1
- Update to first stable release 1.0.0

* Sun Apr 15 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.060.12-4
- add missing posttrans scriptlet

* Mon Feb 20 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.060.12-3
- re-add downstream desktop file
- remove extra .bankdir file

* Sun Feb 19 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.060.12-2
- use upstream desktop and icon files
- fix missing parameters in upstream desktop file
- actually remove FLTK patch

* Sun Jan  8 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.060.12-1
- update to new upstream release 0.060.12
- remove FLTK 1.3 patch

* Mon Aug 29 2011 Adam Huffman <bloch@verdurin.com> - 0.060.10-2
- add patch from Brendan Jones to fix compilation with FLTK 1.3

* Sun Apr 17 2011 Adam Huffman <bloch@verdurin.com> - 0.060.10-1
- new upstream release with further licensing clarification

* Mon Apr 11 2011 Adam Huffman <bloch@verdurin.com> - 0.060.9-1
- new upstream release with licence clarification

* Sun Apr 10 2011 Adam Huffman <bloch@verdurin.com> - 0.060.8-2
- add COPYING and notes to docs

* Sat Apr  9 2011 Adam Huffman <bloch@verdurin.com> - 0.060.8-1
- new upstream release 0.060.8
- add boost-devel BR
- consistent use of macros
- fix directory permissions for banks/presets

* Sun Jun 20 2010 Adam Huffman <bloch@verdurin.com> - 0.058-1
- desktop file and icon added

* Sun May 16 2010 Adam Huffman <bloch@verdurin.com> - 0.056-1
- new upstream release, fixing PAD synth patch problems

* Sun Mar 28 2010 Adam Huffman <bloch@verdurin.com> - 0.055.6-1
- new upstream bugfilx release

* Sat Mar 13 2010 Adam Huffman <bloch@verdurin.com> - 0.055.3-1
- initial version

