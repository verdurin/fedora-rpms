%global packname  limma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.8.1
Release:          2%{?dist}
Summary:          Linear models for microarray data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/limma.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R >= 2.3.0 R-methods 
#Requires:         R-affy R-MASS R-org.Hs.eg.db R-splines R-statmod >= 1.2.2 R-vsn 
Requires:         R-affy R-MASS R-splines R-statmod >= 1.2.2  
#BuildRequires:    R-devel tex(latex) R >= 2.3.0 R-methods R-affy R-MASS R-org.Hs.eg.db R-splines R-statmod >= 1.2.2 R-vsn
BuildRequires:    R-devel tex(latex) R >= 2.3.0 R-methods R-affy R-MASS R-splines R-statmod >= 1.2.2

%description
Data analysis, linear models and differential expression for microarray

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
# Don't check for unnecessary dependencies
#%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> - 3.8.1-2
- remove unnecessary reqs

* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> 3.8.1-1
- initial package for Fedora
