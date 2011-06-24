%global packname  Rsamtools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          2%{?dist}
Summary:          Import aligned bam file format sequences into r / biocon

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/Rsamtools.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-IRanges >= 1.5.56 R-GenomicRanges >= 0.1.0 R-Biostrings >= 2.15.0 
#Avoid circular dependencies
#Requires:         R-ShortRead R-GenomicFeatures R-KEGG.db 
BuildRequires:    R-devel tex(latex) R-methods R-IRanges-devel >= 1.5.56 R-GenomicRanges >= 0.1.0 
BuildRequires:	  R-Biostrings-devel >= 2.15.0 

%description
This package provides an interface to the 'samtools' utilities for
manipulating SAM (Sequence Alignment / Map) format files. Facilities
currently available include flexible file input.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
#%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/libs


%changelog
* Wed Jun 15 2011 Adam Huffman <bloch@verdurin.com> - 1.0.8-2
- trim reqs. to avoid circular dependencies

* Wed Jun 15 2011 Adam Huffman <bloch@verdurin.com> 1.0.8-1
- initial package for Fedora
- disable check to avoid circular dependencies
