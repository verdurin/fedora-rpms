%global packname  gplots
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.10.1
Release:          1%{?dist}
Summary:          Various r programming tools for plotting data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/gplots/index.html
Source0:          http://cran.r-project.org/src/contrib/gplots_2.10.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R >= 2.10 R-gtools R-gdata R-stats R-caTools R-grid R-KernSmooth 
Requires:         R-gtools 
BuildRequires:    R-devel tex(latex) R >= 2.10 R-gtools R-gdata R-stats R-caTools R-grid R-KernSmooth R-gtools

%description
Various R programming tools for plotting data

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/ChangeLog


%changelog
* Fri Oct 14 2011 Adam Huffman <bloch@verdurin.com> - 2.10.1-1
- add missing %%files entries
- initial package for Fedora
