Name:		cufflinks
Version:	1.1.0
Release:	1%{?dist}
Summary:	RNA-Seq transcript assembly, differential expression/regulation

Group:		Applications/Engineering
License:	Boost
URL:		http://cufflinks.cbcb.umd.edu/
Source0:	http://cufflinks.cbcb.umd.edu/downloads/%{name}-%{version}.tar.gz
Patch0:		%{name}-bam-header.patch
Patch1:		%{name}-boost-thread.patch
Patch2:		%{name}-boost141-headers.patch
Patch3:		%{name}-boost141-common-headers.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	boost141-devel samtools-devel zlib-devel
BuildRequires:	autoconf automake python-devel


%description 
Cufflinks assembles transcripts, estimates their abundances, and tests
for differential expression and regulation in RNA-Seq samples. It
accepts aligned RNA-Seq reads and assembles the alignments into a
parsimonious set of transcripts. Cufflinks then estimates the relative
abundances of these transcripts based on how many reads support each
one.

Cufflinks is a collaborative effort between the Laboratory for
Mathematical and Computational Biology, led by Lior Pachter at UC
Berkeley, Steven Salzberg's group at the University of Maryland Center
for Bioinformatics and Computational Biology, and Barbara Wold's lab
at Caltech.

%prep
%setup -q
#Look for BAM headers in the correct Fedora location
%patch0 -p1 -b .cufflinks-bam-header.patch
%patch1 -p1 -b .cufflinks-boost-thread.patch
#Look for EPEL Boost 141 headers in the correct location
%patch2 -p1 -b .cufflinks-boost141-headers.patch
#More Boost141 fixes for common.h for EPEL
%patch3 -p1 -b .cufflinks-boost141-common-headers.patch

%build
autoreconf
%configure --includedir="/usr/include/boost141"
make %{?_smp_mflags} "CPPFLAGS+=" -I/usr/include/boost141 -I/usr/include""


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README AUTHORS LICENSE
%{_bindir}/*


%changelog
* Wed Nov 23 2011 Adam Huffman <bloch@verdurin.com> - 1.1.0-1
- add patch for config.h for Boost141 on EPEL5

* Tue Nov 22 2011 Adam Huffman <bloch@verdurin.com> - 1.1.0-1
- new upstream release 1.1.0

* Mon Aug 22 2011 Adam Huffman <bloch@verdurin.com> - 1.0.3-2
- better EPEL5 fixes for boost141

* Mon Jun  6 2011 Adam Huffman <bloch@verdurin.com> - 1.0.3-1
- new upstream release

* Sun May  8 2011 Adam Huffman <bloch@verdurin.com> - 1.0.1-1
- new upstream release
- add python BR
- fix header location patch
- separate Boost thread patch

* Mon Apr  4 2011 Adam Huffman <bloch@verdurin.com> - 0.9.3-1
- initial version
- patch to fix bam.h header search and to link boost_thread-mt
