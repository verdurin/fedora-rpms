%global packname  mclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.4.10
Release:          2%{?dist}
Summary:          Model-based clustering / normal mixture modeling

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/mclust/index.html
Source0:          http://cran.r-project.org/src/contrib/mclust_3.4.10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R >= 2.2.0 R-stats R-utils 
Requires:         R-mix 
BuildRequires:    R-devel tex(latex) R >= 2.2.0 R-stats R-utils R-mix


%description
Model-based clustering and normal mixture modeling including Bayesian

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
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/cite


%changelog
* Fri Oct 14 2011 Adam Huffman <bloch@verdurin.com> - 3.4.10-2
- remove unnecessary %%files entries
- add missing %%files entries

* Thu Oct 13 2011 Adam Huffman <bloch@verdurin.com> - 3.4.10-2
- reinstate R-mix BR

* Thu Oct 13 2011 Adam Huffman <bloch@verdurin.com> 3.4.10-1
- initial package for Fedora
