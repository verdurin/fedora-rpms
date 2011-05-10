%global packname  ArrayExpressHTS


%global rlibdir %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Arrayexpress high throughput sequencing package

Group:            Applications/Engineering 
License:          Artistic License 2.0
URL:              http://www.ebi.ac.uk/Tools/rwiki/
Source0:          http://www.ebi.ac.uk/Tools/rcloud/downloads/ArrayExpressHTS_1.0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-svMisc R-sampling R-xtable R-DESeq R-ArrayExpress R-RColorBrewer R-biomaRt 

BuildRequires:    R-devel tex(latex) R-svMisc R-sampling R-xtable R-DESeq R-ArrayExpress R-RColorBrewer R-biomaRt 

%description
RNA Sequencing Processing Pipeline and Analysis

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
* Tue Apr 05 2011 Adam Huffman <bloch@verdurin.com> 1.0-1
- initial package for Fedora
