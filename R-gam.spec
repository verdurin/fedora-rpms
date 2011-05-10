%global packname  gam
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.04
Release:          1%{?dist}
Summary:          Generalized additive models

Group:            Applications/Engineering 
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/gam/index.html
Source0:          http://cran.r-project.org/src/contrib/gam_1.04.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-splines 
Requires:         R-akima 
BuildRequires:    R-devel tex(latex) R-stats R-splines R-akima

%description
Functions for fitting and working with generalized additive models, as
described in chapter 7 of "Statistical Models in S" (Chambers and Hastie
(eds), 1991), and "Generalized Additive Models" (Hastie and Tibshirani,

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
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs

%changelog
* Tue Apr 19 2011 Adam Huffman <bloch@verdurin.com> 1.04-1
- initial package for Fedora
