%global packname  nws
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.7.0.1
Release:          1%{?dist}
Summary:          R functions for networkspaces and sleigh

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/nws/index.html
Source0:          http://cran.r-project.org/src/contrib/nws_1.7.0.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R >= 2.1 R-methods 

BuildRequires:    R-devel tex(latex) R >= 2.1 R-methods 

%description
Provides coordination and parallel execution facilities, as well as
limited cross-language data exchange, using the netWorkSpaces server
developed by REvolution Computing

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/README.sleigh
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bin
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/examples


%changelog
* Mon Oct 24 2011 Adam Huffman <bloch@verdurin.com> 1.7.0.1-1
- initial package for Fedora
