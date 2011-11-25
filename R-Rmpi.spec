%global packname  Rmpi
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.9
Release:          1%{?dist}
Summary:          Interface (wrapper) to mpi (message-passing interface)

Group:            Applications/Engineering 
License:          GPLv2+
URL:              http://cran.r-project.org/web/packages/Rmpi/index.html
Source0:          http://cran.r-project.org/src/contrib/Rmpi_0.5-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R >= 2.2.0 
Requires:         R-rsprng R-rlecuyer 
BuildRequires:    R-devel tex(latex) R >= 2.2.0 R-rsprng R-rlecuyer

%description
Rmpi provides an interface (wrapper) to MPI APIs. It also provides
interactive R slave environment.

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
* Mon Oct 24 2011 Adam Huffman <bloch@verdurin.com> 0.5.9-1
- initial package for Fedora
