%global packname  SciViews
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          Sciviews gui api - main package

Group:            Applications/Engineering 
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/SciViews/index.html
Source0:          http://cran.r-project.org/src/contrib/SciViews_0.9-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R >= 2.6.0 R-stats R-grDevices R-graphics R-MASS 

BuildRequires:    R-devel tex(latex) R >= 2.6.0 R-stats R-grDevices R-graphics R-MASS
BuildRequires:	  R-ellipse

Provides:	  R-svGUI R-svMisc R-svUnit R-svSocket

%description
Functions to install SciViews additions to R, and more (various) tools

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
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/LICENSE

%changelog
* Tue Apr 19 2011 Adam Huffman <bloch@verdurin.com> 0.9.2-1
- initial package for Fedora
