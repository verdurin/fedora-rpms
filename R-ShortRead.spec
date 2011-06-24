%global packname  ShortRead
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.2
Release:          1%{?dist}
Summary:          Base classes and methods for high-throughput short-read 

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/ShortRead.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-IRanges >= 1.5.65 R-GenomicRanges R-Biostrings >= 2.13.52 R-lattice R-Rsamtools 
Requires:         R-biomaRt 
BuildRequires:    R-devel tex(latex) R-methods R-IRanges-devel >= 1.5.65 R-GenomicRanges 
BuildRequires:	  R-Biostrings-devel >= 2.13.52 R-lattice R-Rsamtools R-biomaRt R-hwriter

%description
Base classes, functions, and methods for representation of
high-throughput, short-read sequencing data.

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
%{_bindir}/R CMD check %{packname}

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
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/template


%changelog
* Wed Jun 15 2011 Adam Huffman <bloch@verdurin.com> 1.6.2-1
- initial package for Fedora
