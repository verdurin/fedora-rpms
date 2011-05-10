%global packname  akima
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.4
Release:          1%{?dist}
Summary:          Interpolation of irregularly spaced data

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/akima/index.html
Source0:          http://cran.r-project.org/src/contrib/akima_0.5-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Linear or cubic spline interpolation for irregular gridded data

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
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs

%changelog
* Tue Apr 19 2011 Adam Huffman <bloch@verdurin.com> 0.5.4-1
- initial package for Fedora
