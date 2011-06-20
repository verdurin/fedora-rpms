%global packname  biomaRt
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.8.0
Release:          4%{?dist}
Summary:          Interface to biomart databases (e.g. ensembl, cosmic ,wo

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/biomaRt.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 
Requires:         R-annotate R-RCurl
BuildRequires:    R-devel tex(latex) R-methods R-annotate R-RCurl

%description
In recent years a wealth of biological data has become available in public
data repositories. Easy access to these valuable data resources and firm
integration with data analysis is needed for comprehensive bioinformatics
data analysis.  biomaRt provides an interface to a growing collection of
databases implementing the BioMart software suite
(http://www.biomart.org). The package enables retrieval of large amounts
of data in a uniform way without the need to know the underlying database
schemas or write complex SQL queries. Examples of BioMart databases are
Ensembl, COSMIC, Uniprot, HGNC, Gramene, Wormbase and dbSNP mapped to
Ensembl. These major databases give biomaRt users direct access to a
diverse set of data and enable a wide range of powerful online queries
from gene annotation to database mining.

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
%{rlibdir}/%{packname}/scripts

%changelog
* Wed Jun 15 2011 Adam Huffman <bloch@verdurin.com> - 2.8.0-4
- proper RCurl fix

* Wed Jun 15 2011 Adam Huffman <bloch@verdurin.com> - 2.8.0-3
- add reqs for RCurl

* Tue May 10 2011 Adam Huffman <bloch@verdurin.comk> - 2.8.0-2
- add R-RCurl BR
- add scripts directory

* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> 2.8.0-1
- initial package for Fedora
