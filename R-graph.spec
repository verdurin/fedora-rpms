%global packname  graph
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          3%{?dist}
Summary:          Graph: a package to handle graph data structures

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/graph/index.html
Source0:          http://cran.r-project.org/src/contrib/graph_1.28.0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R >= 2.6.0 R-methods 
Requires:         R-SparseM >= 0.36 R-XML R-RUnit 
BuildRequires:    R-devel tex(latex) R >= 2.6.0 R-methods R-RUnit

%description
A package that implements some simple graph handling capabilities.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/GXL
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/perf
%{rlibdir}/%{packname}/Scripts
%{rlibdir}/%{packname}/unitTests

%changelog
* Wed Apr 20 2011 Adam Huffman <adam@elstir.smith.man.ac.uk> - 1.28.0-3
- remove RBGL reqs

* Wed Apr 20 2011 Adam Huffman <adam@elstir.smith.man.ac.uk> - 1.28.0-2
- remove extra BRs

* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> 1.28.0-1
- initial package for Fedora
