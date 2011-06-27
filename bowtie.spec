Name:		bowtie
Version:	0.12.7
Release:	2%{?dist}
Summary:	An ultrafast, memory-efficient short read aligner

Group:		Applications/Engineering
License:	Artistic 2.0
URL:		http://bowtie-bio.sourceforge.net/index.shtml
Source0:	http://downloads.sourceforge.net/%{name}-bio/%{name}-%{version}-src.zip
Patch0:		%{name}-script-shebang.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description

Bowtie, an ultrafast, memory-efficient short read aligner for short
DNA sequences (reads) from next-gen sequencers. Please cite: Langmead
B, et al. Ultrafast and memory-efficient alignment of short DNA
sequences to the human genome. Genome Biol 10:R25.

%prep
%setup -q

%patch0 -p1 

%build
make %{?_smp_mflags} -p EXTRA_FLAGS="%{optflags}"


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/bowtie


install -m 0755 bowtie %{buildroot}/%{_bindir}
install -m 0755 bowtie-build %{buildroot}/%{_bindir}
install -m 0755 bowtie-inspect %{buildroot}/%{_bindir}

cp -a reads %{buildroot}/%{_datadir}/bowtie/
cp -a indexes %{buildroot}/%{_datadir}/bowtie/
cp -a genomes %{buildroot}/%{_datadir}/bowtie/
cp -a scripts %{buildroot}/%{_datadir}/bowtie/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc MANUAL NEWS VERSION AUTHORS TUTORIAL doc/
%dir %{_datadir}/bowtie
%{_bindir}/bowtie
%{_bindir}/bowtie-build
%{_bindir}/bowtie-inspect
%{_datadir}/bowtie/genomes
%{_datadir}/bowtie/indexes
%{_datadir}/bowtie/reads
%{_datadir}/bowtie/scripts

%changelog
* Mon Jun 27 2011 Adam Huffman <bloch@verdurin.com> - 0.12.7-2
- add missing doc/ 
- add patch to fix Perl script without shebang

* Mon Sep 13 2010 Adam Huffman <bloch@verdurin.com> - 0.12.7-1
- new upstream release 0.12.7
- changelog at http://bowtie-bio.sourceforge.net/index.shtml

* Tue Aug 31 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-3
- really fix compilation flags

* Wed Aug 25 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-2
- fix compilation flags

* Mon Aug  2 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-1
- initial version

