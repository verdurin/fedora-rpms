Name:		srma
Version:	0.1.15
Release:	1%{?dist}
Summary:	Short Read Micro re-Aligner

Group:		Applications/Engineering
License:	GPLv2
URL:		http://srma.sf.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.jar
BuildRoot:	a%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Requires:	java >= 1:1.6.0
Requires:	jpackage-utils


%description

SRMA is a short read micro re-aligner for next-generation high
throughput sequencing data.  Sequence alignment algorithms examine
each read independently. When indels occur towards the ends of reads,
the alignment can lead to false SNPs as well as improperly placed
indels. This tool aims to perform a re-alignment of each read to a
graphical representation of all alignments within a local region to
provide a better overall base-resolution consensus.  Currently this
tool works well with and has been tested on 30x diploid coverage
genome sequencing data from Illumina and ABI SOLiD technology. This
tool may not work well with 454 data, as indels are a significant
error mode for 454 data.

%prep

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_javadir}
cp %{SOURCE0} %{buildroot}%{_javadir}/%{name}.jar


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_javadir}/*



%changelog
* Thu Aug 11 2011 Adam Huffman <bloch@verdurin.com> - 0.1.15-1
- initial version

