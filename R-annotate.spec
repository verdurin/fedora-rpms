%global packname  annotate
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.30.1
Release:          1%{?dist}
Summary:          Annotation for microarrays

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/annotate.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R >= 2.4.0 R-AnnotationDbi >= 0.1.15 
Requires:         R-Biobase R-Biostrings >= 2.4.4 R-tkWidgets R-XML >= 0.92-2   
#BuildRequires:    R-devel tex(latex) R >= 2.4.0 R-AnnotationDbi >= 0.1.15 R-Biobase R-hgu95av2.db R-genefilter R-Biostrings >= 2.4.4 R-rae230a.db R-rae230aprobe R-tkWidgets R-XML >= 0.92-2 R-GO.db R-org.Hs.eg.db R-org.Mm.eg.db R-hom.Hs.inp.db

BuildRequires:    R-devel tex(latex) R >= 2.4.0 R-AnnotationDbi >= 0.1.15 R-Biobase 
BuildRequires:	  R-Biostrings >= 2.4.4 R-tkWidgets R-XML >= 0.92-2 R-xtable

%description
Using R enviroments for annotation.

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
# Ignore unnecessary dependencies
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
%{rlibdir}/%{packname}/misc


%changelog
* Fri Oct 14 2011 Adam Huffman <bloch@verdurin.com> - 1.30.1-1
- update to latest upstream release 1.30.1

* Wed Apr 20 2011 Adam Huffman <adam@elstir.smith.man.ac.uk> - 1.26.1-3
- remove genefilter reqs

* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> - 1.26.1-2
- remove problematic BR and Reqs

* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> 1.26.1-1
- initial package for Fedora
