%global packname  lpSolve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.6.5
Release:          2%{?dist}
Summary:          Interface to lp_solve v. 5.5 to solve linear/integer pro

Group:            Applications/Engineering 
License:          LGPLv2
URL:		  http://cran.r-project.org/web/packages/lpSolve/index.html
Source0:          http://cran.r-project.org/src/contrib/lpSolve_5.6.5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Lp_solve is freely available (under LGPL 2) software for solving linear,
integer and mixed integer programs. In this implementation we supply a
"wrapper" function in C and some R functions that solve general
linear/integer problems, assignment problems, and transportation problems.
This version calls lp_solve version 5.5.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs/lpSolve.so


%changelog
* Tue Apr 19 2011 Adam Huffman <adam@elstir.smith.man.ac.uk> - 5.6.5-2
- don't delete library, needed by R-sampling

* Tue Apr 19 2011 Adam Huffman <bloch@verdurin.com> 5.6.5-1
- initial package for Fedora
