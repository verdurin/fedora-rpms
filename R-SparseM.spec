%global packname  SparseM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.88
Release:          1%{?dist}
Summary:          Sparse linear algebra

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/SparseM/index.html
Source0:          http://cran.r-project.org/src/contrib/SparseM_0.88.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R >= 2.4.1 R-methods R-stats R-utils 

BuildRequires:    R-devel tex(latex) R >= 2.4.1 R-methods R-stats R-utils
BuildRequires:	  texinfo-tex

%description
Basic linear algebra for sparse matrices

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/libs


%changelog
* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> 0.88-1
- initial package for Fedora
