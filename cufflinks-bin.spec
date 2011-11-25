%global		tarname	"cufflinks"
%global 	debug_package %{nil}
Name:		cufflinks-bin
Version:	1.0.3
Release:	1%{?dist}
Summary:	RNA-Seq transcript assembly, differential expression/regulation

Group:		Applications/Engineering
License:	Boost
URL:		http://cufflinks.cbcb.umd.edu/
Source0:	http://cufflinks.cbcb.umd.edu/downloads/cufflinks-1.0.3.Linux_x86_64.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


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

This is a binary-only package.

%prep
%setup -q -n %tarname-%{version}.Linux_x86_64


%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 cuff* %{buildroot}%{_bindir}
install -m 0755 gffread %{buildroot}%{_bindir}
install -m 0755 gtf_to_sam %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README LICENSE AUTHORS
%{_bindir}/cuff*
%{_bindir}/gffread
%{_bindir}/gtf_to_sam



%changelog
* Mon Aug 22 2011 Adam Huffman <bloch@verdurin.com> - 1.0.3-1
- initial version of binary package

