%global		buildtemp %{_builddir}/%{name}-%{version}

Name:		seqan
Version:	1.3
Release:	3%{?dist}
Summary:	Biological sequence analysis library

Group:		Applications/Engineering
License:	BSD with advertising
URL:		http://seqan.de/
Source0:	http://www.seqan.de/uploads/media/Seqan_Release_%{version}.zip
Source1:	%{name}-debian-manpages.tar
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	python-devel >= 2.5
BuildRequires:	cmake
BuildRequires:	zlib-devel
BuildRequires:	samtools-devel
BuildRequires:	dos2unix

%description

SeqAn is an open source C++ library of efficient algorithms and data
structures for the analysis of sequences with the focus on biological
data. Our library applies a unique generic design that guarantees high
performance, generality, extensibility, and integration with other
libraries. SeqAn is easy to use and simplifies the development of new
software tools with a minimal loss of performance.

%package devel
Summary: Header files and libraries for compiling against %{name}
Group:   Development/System
Requires: %name = %version-%release

%description devel

Header files for compiling against %{name}


%prep
%setup -q -c %{name}-%{version}

#Fix incorrect file encodings
dos2unix doc/dddoc.js
dos2unix doc/%{name}-%{version}/README


%build
cd cmake
%cmake -DCMAKE_SKIP_RPATH=YES .
make %{?_smp_mflags}


%install
rm -rf %{buildroot}


mkdir -p %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/dfi %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/insegt %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/mason %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/micro_razers %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/pair_align %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/param_chooser %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/rabema %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/razers %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/razers2 %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/read_analyzer %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/rep_sep %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/sak %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/seqan_tcoffee %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/seqcons %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/snp_store %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/splazers %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/stellar %{buildroot}%{_bindir}
install -p %{buildtemp}/cmake/apps/tree_recon %{buildroot}%{_bindir}

mkdir -p %{buildroot}/%{_includedir}/%{name}
chmod -R -x %{buildtemp}/%{name}
cp -a %{buildtemp}/%{name} %{buildroot}/%{_includedir}/
rm %{buildroot}/%{_includedir}/%{name}/LICENSE

mkdir -p %{buildroot}%{_mandir}/man1
cd %{buildroot}%{_mandir}/man1
tar xvf %{SOURCE1}


%clean
rm -rf %{buildroot}

%check
ctest

%files
%defattr(-,root,root,-)
%doc README 
%{_bindir}/dfi
%{_bindir}/insegt
%{_bindir}/mason
%{_bindir}/micro_razers
%{_bindir}/pair_align
%{_bindir}/param_chooser
%{_bindir}/rabema
%{_bindir}/razers
%{_bindir}/razers2
%{_bindir}/read_analyzer
%{_bindir}/rep_sep
%{_bindir}/sak
%{_bindir}/seqan_tcoffee
%{_bindir}/seqcons
%{_bindir}/snp_store
%{_bindir}/splazers
%{_bindir}/stellar
%{_bindir}/tree_recon
%{_mandir}/man1/dfi.1*
%{_mandir}/man1/micro_razers.1*
%{_mandir}/man1/pair_align.1*
%{_mandir}/man1/razers.1*
%{_mandir}/man1/seqan_tcoffee.1*
%{_mandir}/man1/seqcons.1*
%{_mandir}/man1/tree_recon.1*

%files devel
%defattr(-,root,root,-)
%doc doc seqan/LICENSE
%{_includedir}/seqan

%changelog
* Fri Jun  3 2011 Adam Huffman <bloch@verdurin.com> - 1.3-3
- add manpages from Debian package
- add -devel subpackage

* Fri Jun  3 2011 Adam Huffman <bloch@verdurin.com> - 1.3-2
- initial version
- boost-devel BR
- remove RPATH
- add zlib and samtools BR

