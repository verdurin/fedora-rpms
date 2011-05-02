Name:		yoshimi
Version:	0.060.10
Release:	1%{?dist}
Summary:	Rewrite of ZynAddSubFx aiming for better JACK support

Group:		Applications/Multimedia
License:	GPLv2+
URL:		http://sourceforge.net/projects/yoshimi
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	yoshimi.desktop
Source2:	yoshimi.svg
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	cmake zlib-devel fontconfig-devel
BuildRequires:	fltk-devel fltk-fluid fftw3-devel
BuildRequires:	mxml-devel alsa-lib-devel libsndfile-devel
BuildRequires:	desktop-file-utils boost-devel

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
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

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


%files
%defattr(-,root,root,-)
%doc 0.060.10.notes COPYING
%{_bindir}/yoshimi
%{_datadir}/%{name}/banks/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/presets/

%changelog
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

