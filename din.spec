Name:		din
Version:	1.5.8.0
Release:	3%{?dist}
Summary:	A musical instrument using multiple Bezier curves

Group:		Applications/Multimedia
License:	GPLv2
URL:		http://www.dinisnoise.org
Source0:	http://din.googlecode.com/files/din-%{version}.tar.gz
Patch0:		din-build.patch
Patch1:		din-libs.patch
Patch2:		din-include.patch
Patch3:		din-data.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	tcl-devel libircclient-devel SDL-devel liblo-devel
BuildRequires:	jack-audio-connection-kit-devel mesa-libGL-devel
BuildRequires:	automake fftw-devel

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
%patch0 -p1
%patch1 -p1
%patch2 -p1 
%patch3 -p1

%build
autoreconf
%configure --localstatedir=/usr/share
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

chmod 0755 %{buildroot}/%{_datadir}/%{name}/m00

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README TODO CHANGELOG AUTHORS COPYING BUGS
%{_bindir}/din
%{_bindir}/checkdotdin
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
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
