%global packname  XML


%global rlibdir %{_libdir}/R/library


Name:		R-%{packname}
Version:	3.2.0
Release:	1%{?dist}
Summary:	Tools for parsing and generating xml within r and s-plus

Group:		Applications/Engineering 
License:	BSD
URL:		http://cran.r-project.org/web/packages/XML/index.html
Source0:	http://cran.r-project.org/src/contrib/XML_3.2-0.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	R >= 1.2.0 R-methods R-utils 
Requires:	R-bitops 
BuildRequires:	R-devel tex(latex) R >= 1.2.0 R-methods R-utils R-bitops
BuildRequires:	libxml2-devel

%description
This package provides many approaches for both reading and creating XML
(and HTML) documents (including DTDs), both local and accessible via HTTP
or FTP. It also offers access to an XPath "interpreter".

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname} \
--configure-args='--with-xml-config=%{_bindir}/xml2-config'
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Don't need Windows file or Subversion files
rm -f %{buildroot}%{rlibdir}/%{packname}/README.windows
rm -rf %{buildroot}%{rlibdir}/%{packname}/exampleData/xinclude/.svn

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}



%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/Docs
%doc %{rlibdir}/%{packname}/exampleData
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs/%{packname}.so

%changelog
* Tue Apr 05 2011 Adam Huffman <bloch@verdurin.com> 3.2.0-1
- initial package for Fedora
- add BR for libxml2-devel
