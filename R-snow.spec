%global packname  snow
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.7
Release:          1%{?dist}
Summary:          Simple network of workstations

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/snow/index.html
Source0:          http://cran.r-project.org/src/contrib/snow_0.3-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R >= 2.12.1 R-utils 
Requires:         R-Rmpi R-rpvm R-rlecuyer R-rsprng R-nws 
#BuildRequires:    R-devel tex(latex) R >= 2.12.1 R-utils R-Rmpi R-rpvm R-rlecuyer R-rsprng R-nws
BuildRequires:    R-devel tex(latex) R >= 2.12.1 R-utils 

%description
Support for simple parallel computing in R.

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
* Fri Oct 14 2011 Adam Huffman <bloch@verdurin.com> 0.3.7-1
- initial package for Fedora
