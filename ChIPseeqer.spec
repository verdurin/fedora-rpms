Name:		ChIPseeqer
Version:	2.0
Release:	1%{?dist}
Summary:	ChIP-seq dataset analysis

Group:		Applications/Engineering
License:	GPLv3  
URL:		http://physiology.med.cornell.edu/faculty/elemento/lab/chipseq.shtml
Source0:	http://physiology.med.cornell.edu/faculty/elemento/lab/CS_files/%{name}-%{version}.tar.gz
#Source1:	http://physiology.med.cornell.edu/faculty/elemento/lab/CS_files/hg18.tar.gz
#Source2:	http://physiology.med.cornell.edu/faculty/elemento/lab/CS_files/Encode.tar.gz
Patch0:		%{name}-qmake-qt4.patch
Patch1:		%{name}-qmake-qt4-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ncurses-devel
BuildRequires:	pcre-devel
BuildRequires:	poppler-qt4-devel
BuildRequires:	qt-devel >= 4.7.2
BuildRequires:	perl-ExtUtils-MakeMaker

#Requires:	perl-IO-Zlib

%description

ChIPseeqer is a computational framework for the analysis of ChIP-seq datasets. 
It includes quality control tools for the raw data and peak detection. 
Moreover, it offers: (1) Gene-level annotation of peaks, (2) Pathways 
enrichment analysis, (3) Regulatory element analysis, using either a de novo 
approach, known or user-defined motifs, (4) Nongenic peak annotation (repeats, 
CpG islands, duplications), (5) Conservation analysis, (6) Clustering analysis, 
(7) Visualization, (8) Integration and comparison across different ChIP-seq 
experiments.

%prep
%setup -q
%patch0 -p1 -b .%{name}-qmake-qt4.patch
%patch1 -p1 -b .%{name}-qmake-qt4-Makefile.patch

%build
cd src
#make %{?_smp_mflags}

make -f Makefile.init
make CFLAGS="%{optflags}"
make dist CFLAGS="%{optflags}"
make tools CFLAGS="%{optflags}"
make gui CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
cd dist
install -m 0755 ChIP* %{buildroot}%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README LICENCE
%{_bindir}/ChIP*


%changelog
* Thu Aug  4 2011 Adam Huffman <bloch@verdurin.com> - 2.0-1
- initial version
- add missing reqs. for perl-IO-Zlib
- patch for qmake-qt4

