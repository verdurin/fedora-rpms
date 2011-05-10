%global packname  genefilter
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.35.0
Release:          1%{?dist}
Summary:          Genefilter: methods for filtering genes from microarray 

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/genefilter.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase >= 1.99.10 R-class R-methods R-tkWidgets
#BuildRequires:    R-devel tex(latex)  R-Biobase >= 1.99.10 R-class R-hgu95av2.db R-methods R-tkWidgets R-ALL
BuildRequires:    R-devel tex(latex)  R-Biobase >= 1.99.10 R-class R-methods R-tkWidgets
BuildRequires:	  R-annotate R-AnnotationDbi R-xtable

%description
Some basic functions for filtering genes

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
%doc %{rlibdir}/%{packname}/COPYING
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/wFun
%{rlibdir}/%{packname}/libs

%changelog
* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> 1.35.0-1
- initial package for Fedora
