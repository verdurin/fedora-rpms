Name:		mmseq
Version:	0.9.10b
Release:	3%{?dist}
Summary:	Haplotype and isoform specific expression estimation for RNA-seq

Group:		Applications/Engineering
License:	GPLv2+
URL:		http://www.bgx.org.uk/software/mmseq.html
Source0:	http://www.bgx.org.uk/software/%{name}_%{version}.zip
Patch0:		mmseq-sam-header.patch
Patch1:		mmseq-flags.patch
Patch2:		mmseq-zlib.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	boost-devel
BuildRequires:	samtools-devel
BuildRequires:	gsl-devel
BuildRequires:	zlib-devel

Requires:	ruby
Requires:	samtools
Requires:	perl

%description
Software for fast, scalable haplotype and isoform expression
estimation using multi-mapping RNA-seq reads.  Example scripts are included.

%prep
%setup -q -n %{name}_%{version}
#Look for samtools headers in the correct location for Fedora
%patch0 -p1 -b .mmseq-sam-header.patch
#Use Fedora compilation headers
%patch1 -p1 -b .mmseq-flags.patch
#Fix zlib linking
%patch2 -p1 -b .mmseq-zlib.patch

#Remove bundled binaries
rm bam2hits*-x86_64
rm mmseq*-x86_64

%build
make %{?_smp_mflags} CXXFLAGS="%{optflags}"


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 bam2hits %{buildroot}%{_bindir}
install -p -m 0755 mmseq %{buildroot}%{_bindir}
install -p -m 0755 *.sh %{buildroot}%{_bindir}
install -p -m 0755 *.rb %{buildroot}%{_bindir}
install -p -m 0755 ensembl_gtf_to_gff.pl %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/bam2hits
%{_bindir}/mmseq
%{_bindir}/fastagrep.sh
%{_bindir}/pileup.sh
%{_bindir}/filterGTF.rb
%{_bindir}/get_isize.rb
%{_bindir}/haploref.rb
%{_bindir}/sam2hits.rb
%{_bindir}/testregexp.rb
%{_bindir}/ensembl_gtf_to_gff.pl

%changelog
* Fri May 27 2011 Adam Huffman <bloch@verdurin.com> - 0.9.10b-3
- patch to deal with zlib better

* Sun May 15 2011 Adam Huffman <bloch@verdurin.com> - 0.9.10b-2
- remove bundled binaries
- remove VERSION
- explicit naming for included scripts

* Sun May  8 2011 Adam Huffman <bloch@verdurin.com> - 0.9.10b-1
- new upstream version
- patch descriptions

* Sun May  8 2011 Adam Huffman <bloch@verdurin.com> - 0.9.9-3
- fix permissions for installed files
- include missing Perl script
- improve description

* Sat Apr  9 2011 Adam Huffman <bloch@verdurin.com> - 0.9.9-2
- fix compilation flags for debuginfo
- include shell and Ruby scripts

* Mon Apr  4 2011 Adam Huffman <bloch@verdurin.com> - 0.9.9-1
- initial version

