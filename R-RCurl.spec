%global packname  RCurl
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          General network (http/ftp/...) client interface for r

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/RCurl/index.html
Source0:          http://cran.r-project.org/src/contrib/RCurl_1.5-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R >= 2.7.0 R-methods R-bitops 
Requires:         R-Rcompression libcurl 
#BuildRequires:    R-devel tex(latex) R >= 2.7.0 R-methods R-bitops R-Rcompression
BuildRequires:    R-devel tex(latex) R >= 2.7.0 R-methods R-bitops libcurl-devel
BuildRequires:	  R-Rcompression

%description
The package allows one to compose general HTTP requests and provides
convenient functions to fetch URIs, get & post forms, etc. and process the
results returned by the Web server. This provides a great deal of control
over the HTTP/FTP/... connection and the form of the request while
providing a higher-level interface than is available just using R socket
connections. Additionally, the underlying implementation is robust and
extensive, supporting FTP/FTPS/TFTP (uploads and downloads), SSL/HTTPS,
telnet, dict, ldap, and also supports cookies, redirects, authentication,

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
* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> 1.5.0-1
- initial package for Fedora
