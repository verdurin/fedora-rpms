%global packname  RBGL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          An interface to the boost graph library

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/RBGL/index.html
Source0:          http://cran.r-project.org/src/contrib/RBGL_1.26.0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph R-methods 
Requires:         R-Rgraphviz 
BuildRequires:    R-devel tex(latex) R-graph R-methods

%description
A fairly extensive and comprehensive interface to the graph algorithms
contained in the BOOST library.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/XML
%{rlibdir}/%{packname}/boostExamples
%{rlibdir}/%{packname}/demos
%{rlibdir}/%{packname}/dot
%{rlibdir}/%{packname}/dtd
%{rlibdir}/%{packname}/fdep.ps
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/data

%changelog
* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> 1.26.0-1
- initial package for Fedora
