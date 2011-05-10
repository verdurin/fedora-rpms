%global packname  Rgraphviz
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.31.0
Release:          1%{?dist}
Summary:          Provides plotting capabilities for r graph objects

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/Rgraphviz.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R >= 2.6.0 R-methods R-utils R-graph R-grid graphviz

BuildRequires:    R-devel tex(latex) R >= 2.6.0 R-methods R-utils R-graph R-grid 
BuildRequires:	  graphviz-devel

%description
Interfaces R with the AT and T graphviz library for plotting R graph
objects from the graph package. Users on all platforms must install
graphviz; see the README file, available in the source distribution of
this file, for details.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/usecases

%changelog
* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> 1.31.0-1
- initial package for Fedora
