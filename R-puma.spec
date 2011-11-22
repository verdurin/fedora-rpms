%global packname  puma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.0
Release:          1%{?dist}
Summary:          Propagating uncertainty in microarray analysis

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/puma.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R >= 2.6.0 R-Biobase >= 2.5.5 R-affy >= 1.23.4 R-graphics R-grDevices R-methods R-stats R-utils R-mclust 
Requires:         R-pumadata R-affydata R-snow R-limma R-annotate R-ROCR 
BuildRequires:    R-devel tex(latex) R >= 2.6.0 R-Biobase >= 2.5.5 R-affy >= 1.23.4 R-graphics R-grDevices R-methods R-stats R-utils R-mclust R-pumadata R-affydata R-snow R-limma R-annotate R-ROCR
# Don't need all these from "sugggests"
#BuildRequires:    R-devel tex(latex) R >= 2.6.0 R-Biobase >= 2.5.5 R-affy >= 1.23.4 R-graphics R-grDevices R-methods R-stats R-utils R-mclust 

#TODO: needs mclust, grDevices in R-core

%description
Most analyses of Affymetrix GeneChip data are based on point estimates of
expression levels and ignore the uncertainty of such estimates. By
propagating uncertainty to downstream analyses we can improve results from
microarray analyses. For the first time, the puma package makes a suite of
uncertainty propagation methods available to a general audience. puma also
offers improvements in terms of scope and speed of execution over
previously available uncertainty propagation methods. Included are
summarisation, differential expression detection, clustering and PCA
methods, together with useful plotting and data manipulation functions.

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


%changelog
* Thu Oct 13 2011 Adam Huffman <bloch@verdurin.com> 2.4.0-1
- initial package for Fedora
