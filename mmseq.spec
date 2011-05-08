Name:		mmseq
Version:	0.9.10b
Release:	1%{?dist}
Summary:	Haplotype and isoform specific expression estimation for RNA-seq

Group:		Applications/Engineering
License:	GPLv2+
URL:		http://www.bgx.org.uk/software/mmseq.html
Source0:	http://www.bgx.org.uk/software/%{name}_%{version}.zip
Patch0:		mmseq-sam-header.patch
Patch1:		mmseq-flags.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	boost-devel samtools-devel gsl-devel zlib-devel

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
%doc AUTHORS VERSION COPYING
%{_bindir}/bam2hits
%{_bindir}/mmseq
%{_bindir}/*.sh
%{_bindir}/*.rb
%{_bindir}/*.pl

%changelog
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

