Name:		tophat
Version:	1.3.0
Release:	1%{?dist}
Summary:	A spliced read mapper for RNA-Seq

Group:		Applications/Engineering
License:	Artistic 2.0
URL:		http://tophat.cbcb.umd.edu/
Source0:	http://tophat.cbcb.umd.edu/downloads/%{name}-%{version}.tar.gz
Patch0:		%{name}-sam-header.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	autoconf automake python-devel samtools-devel zlib-devel
BuildRequires:	dos2unix

Requires:	bowtie

%description
TopHat is a fast splice junction mapper for RNA-Seq reads. It aligns
RNA-Seq reads to mammalian-sized genomes using the ultra
high-throughput short read aligner Bowtie, and then analyzes the
mapping results to identify splice junctions between exons.

TopHat is a collaborative effort between the University of Maryland
Center for Bioinformatics and Computational Biology and the University
of California, Berkeley Departments of Mathematics and Molecular and
Cell Biology.

%prep
%setup -q
%patch0 -p1 -b .tophat-sam-header.patch
#Fix incorrect permissions and line-endings
#dos2unix src/SeqAn-1.1/seqan/modifier/modifier_reverse.h
#dos2unix src/SeqAn-1.1/seqan/modifier/modifier_view.h
#dos2unix src/SeqAn-1.1/seqan/modifier/modifier_functors.h
#dos2unix src/SeqAn-1.1/seqan/modifier/modifier_string.h
#dos2unix src/SeqAn-1.1/seqan/modifier/modifier_shortcuts.h
#dos2unix src/SeqAn-1.1/seqan/modifier/modifier_iterator.h

#chmod -x src/align_status.h
#chmod -x src/deletions.cpp
#chmod -x src/SeqAn-1.1/seqan/modifier/modifier_functors.h
#chmod -x src/SeqAn-1.1/seqan/modifier/modifier_string.h
#chmod -x src/deletions.h
#chmod -x src/align_status.cpp
#chmod -x src/SeqAn-1.1/seqan/modifier/modifier_shortcuts.h
#chmod -x src/insertions.cpp
#chmod -x src/SeqAn-1.1/seqan/modifier/modifier_iterator.h
#chmod -x src/insertions.h
#chmod -x src/SeqAn-1.1/seqan/modifier/modifier_reverse.h
#chmod -x src/SeqAn-1.1/seqan/modifier/modifier_view.h

%build
autoreconf
%configure
# normal SMP flags break build
make 


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README THANKS
%{_bindir}/*


%changelog
* Mon Jun  6 2011 Adam Huffman <bloch@verdurin.com> - 1.3.0-1
- new upstream release

* Wed May 18 2011 Adam Huffman <bloch@verdurin.com> - 1.2.0-2
- remove Make smp flags to fix build
- fix permissions and file format problems

* Tue May 17 2011 Adam Huffman <bloch@verdurin.com> - 1.2.0-1
- initial version

