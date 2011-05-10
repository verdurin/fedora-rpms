%global packname  geneplotter
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.31.0
Release:          1%{?dist}
Summary:          Graphics related functions for bioconductor

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/geneplotter.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase >= 2.5.5 R-annotate R-lattice 
#Requires:         R-Biobase >= 2.5.5 R-Rgraphviz R-annotate R-fibroEset R-hgu95av2.db R-hu6800.db R-hgu133a.db 
Requires:         R-Rgraphviz R-annotate R-fibroEset  
#BuildRequires:    R-devel tex(latex) R-Biobase >= 2.5.5 R-annotate R-lattice R-Rgraphviz R-annotate R-fibroEset R-hgu95av2.db R-hu6800.db R-hgu133a.db
BuildRequires:    R-devel tex(latex) R-Biobase >= 2.5.5 R-annotate R-lattice R-Rgraphviz
BuildRequires:	  R-annotate R-RColorBrewer R-xtable

%description
Some basic functions for plotting genetic data

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
%doc %{rlibdir}/%{packname}/COPYING
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data


%changelog
* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> 1.31.0-1
- initial package for Fedora
