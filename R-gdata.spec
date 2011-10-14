%global packname  gdata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.8.2
Release:          2%{?dist}
Summary:          Various r programming tools for data manipulation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/gdata/index.html
Source0:          http://cran.r-project.org/src/contrib/gdata_2.8.2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R >= 2.6.0 

BuildRequires:    R-devel tex(latex) R >= 2.6.0 R-gtools
BuildRequires:	  perl-Spreadsheet-ParseExcel
# Perl Excel modules required




%description
Various R programming tools for data manipulation

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
%{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/bin
%{rlibdir}/%{packname}/xls
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/perl


%changelog
* Fri Oct 14 2011 Adam Huffman <bloch@verdurin.com> - 2.8.2-2
- re-add perl subdirectory to meet R-gplots reqs.

* Fri Oct 14 2011 Adam Huffman <bloch@verdurin.com> - 2.8.2-1
- add R-gtools BR
- remove perl/ subdirectory and add missing %%files items
- add perl-Spreadsheet-ParseExcel BR, needed for examples

* Fri Oct 14 2011 Adam Huffman <bloch@verdurin.com> 2.8.2-1
- initial package for Fedora
