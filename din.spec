Name:		din
Version:	3.5
Release:	1%{?dist}
Summary:	A musical instrument using multiple Bezier curves

Group:		Applications/Multimedia
License:	GPLv2
URL:		http://www.dinisnoise.org
Source0:	http://din.googlecode.com/files/din-%{version}.tar.gz
# Patches to use Fedora rather than Debian-specific library and header paths
Patch0:		din-build.patch
Patch1:		din-libs.patch
Patch2:		din-include.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	tcl-devel 
BuildRequires:	libircclient-devel
BuildRequires:	SDL-devel
BuildRequires:	liblo-devel
BuildRequires:	jack-audio-connection-kit-devel 
BuildRequires:	mesa-libGL-devel
BuildRequires:	automake 
BuildRequires:	fftw-devel
BuildRequires:	desktop-file-utils

%description

din is a software musical instrument and audio synthesizer. Bezier
curves are used to draw and sculpt waveforms, create gating and
modulation (FM and AM) patterns, and create delay feedback and volume
patterns. You can also create an unlimited number of drones and sculpt
their waveforms. It uses JACK to output audio, and supports MIDI, OSC
and IRC bot for input. din can be extended and customized with Tcl/Tk
scripts.


%prep
%setup -q
%patch0 -p1 -b .din-build
%patch1 -p1 -b .din-libs
%patch2 -p1 -b .din-include


%build
autoreconf
%configure --localstatedir=%{_datadir}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

chmod 0755 %{buildroot}/%{_datadir}/%{name}/m00

desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/%{name}.desktop 

%clean
rm -rf %{buildroot}

%post
/bin/touch --no-create %{_datadir}/pixmaps &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/pixmaps &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/pixmaps &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/pixmaps &>/dev/null || :

%files
%defattr(-,root,root,-)
%doc README TODO CHANGELOG AUTHORS COPYING BUGS
%{_bindir}/din
%{_bindir}/checkdotdin
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
* Wed Aug 22 2012  <bloch@verdurin.com> - 3.5-1
- Update to upstream 3.5 releaes
- .desktop file and icon now provided

* Wed Jan 11 2012 Adam Huffman <verdurin@fedoraproject.org> - 1.9.2-1
- update to 1.9.2
- minor spec formatting cleanups

* Wed Nov 16 2011 Adam Huffman <bloch@verdurin.com> - 1.9-1
- upstream release 1.9
- update din-build.patch

* Sun Jul 31 2011 Adam Huffman <bloch@verdurin.com> - 1.6.6-1
- new upstream release 1.6.6

* Mon Jul 25 2011 Adam Huffman <bloch@verdurin.com> - 1.6.5-1
- new upstream release 1.6.5
- http://dinisnoise.org/release_notes/

* Tue Jun 21 2011 Adam Huffman <bloch@verdurin.com> - 1.6.3-1
- new upstream release 1.6.3

* Sun May  8 2011 Adam Huffman <bloch@verdurin.com> - 1.5.9-1
- new upstream release

* Fri Apr 29 2011 Adam Huffman <bloch@verdurin.com> - 1.5.8.0-3
- official description

* Fri Apr 29 2011 Adam Huffman <bloch@verdurin.com> - 1.5.8.0-2
- BR for new subpackage libircclient-devel

* Fri Apr 29 2011 Adam Huffman <bloch@verdurin.com> - 1.5.8.0-1
- update patches for new version
- new upstream release
- add fftw and automake BR

* Sun Feb 13 2011 Adam Huffman <bloch@verdurin.com> - 1.4.3-1
- initial version
- look in Fedora location for Tcl headers
- store data in /usr/share, not /var
