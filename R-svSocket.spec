%global packname  svSocket


%global rlibdir %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.51
Release:          4%{?dist}
Summary:          Sciviews gui api - r socket server

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/svSocket/index.html
Source0:          http://cran.r-project.org/src/contrib/svSocket_0.9-51.tar.gz
#Patch0:		  %{name}-tclsh.patch
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R >= 2.6.0 tcl

BuildRequires:    R-devel tex(latex) R >= 2.6.0 R-svMisc

%{?filter_setup:
%filter_from_requires /usr/local/bin/tclsh8.4
%filter_setup
}


%description
Implements a simple socket server allowing to connect GUI clients to R

%prep
%setup -q -c -n %{packname}
#Fix hardcoded tclsh path
#%patch0 -p1 -b .%{name}-tclsh

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/etc

%changelog
* Wed Jun 15 2011 Adam Huffman <bloch@verdurin.com> - 0.9.51-4
- better fix for incorrect Tcl path

* Tue May 10 2011 Adam Huffman <bloch@verdurin.com> - 0.9.51-3
- add patch for hardcoded Tcl path
- filter incorrect Tcl reqs.

* Tue May 10 2011 Adam Huffman <bloch@verdurin.com> - 0.9.51-2
- add R-svMisc BR
- add missing files

* Tue Apr 05 2011 Adam Huffman <bloch@verdurin.com> 0.9.51-1
- initial package for Fedora
