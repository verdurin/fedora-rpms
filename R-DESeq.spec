%global packname  DESeq
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          3%{?dist}
Summary:          Digital gene expresion analysis based on the negative bi

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://bioconductor.org/packages/release/bioc/html/DESeq.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-locfit R-genefilter R-geneplotter

BuildRequires:    R-devel tex(latex) R-Biobase R-locfit R-genefilter R-geneplotter
BuildRequires:	  R-xtable R-RColorBrewer

%description
Estimate variance-mean dependence in count data from high-throughput
sequencing assays and test for differential expression based on a model
using the negative binomial distribution

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/extra

%changelog
* Wed Jun 15 2011 Adam Huffman <bloch@verdurin.com> - 1.5.0-3
- add geneplotter reqs

* Wed Jun 15 2011 Adam Huffman <bloch@verdurin.com> - 1.5.0-2
- add req for genefilter

* Tue Apr 19 2011 Adam Huffman <bloch@verdurin.com> 1.5.0-1
- initial package for Fedora
