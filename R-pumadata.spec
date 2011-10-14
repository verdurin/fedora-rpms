%global packname  pumadata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Various data sets for use with the puma package

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/pumadata.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Patch0:		  %{name}-circular-dependency-fix.patch
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R >= 2.4.0 R-affy >= 1.23.4 R-Biobase >= 2.5.5 R-puma 

#BuildRequires:    R-devel tex(latex) R >= 2.4.0 R-affy >= 1.23.4 R-Biobase >= 2.5.5 R-puma 
#Try removing circular dependency on puma
BuildRequires:    R-devel tex(latex) R >= 2.4.0 R-affy >= 1.23.4 R-Biobase >= 2.5.5 

%description
This is a simple data package including various data sets derived from the
estrogen data for use with the puma (Propagating Uncertainty in Microarray
Analysis) package.

%prep
%setup -q -c -n %{packname}
%patch0 -p0 -b .%{name}-circular-dependency-fix.patch

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
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
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/data


%changelog
* Fri Oct 14 2011 Adam Huffman <bloch@verdurin.com> - 1.0.3-2
- remove circular dependency on R-puma
- fix %%files
- disable %%check to work around circular dependency

* Fri Oct 14 2011 Adam Huffman <bloch@verdurin.com> 1.0.3-1
- initial package for Fedora
