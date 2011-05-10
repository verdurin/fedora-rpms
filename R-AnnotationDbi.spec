%global packname  AnnotationDbi
%global Rvers     2.11.0

Name:             R-%{packname}
Version:          1.14.1
Release:          1%{dist}
Summary:          Annotation Database Interface

Group:            Applications/Engineering 
License:          Artistic 2.0 
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:        noarch

# The suggested requirement are not added here based on:
# - the amount
# - they are mostly database (content)
# - circular dependancies (such as with hgu95av2)
Requires:         R-core >= %{Rvers} R-methods R-utils 
Requires:         R-Biobase R-DBI R-RSQLite
BuildRequires:    R-devel >= %{Rvers} tex(latex) R-methods 
BuildRequires:    R-utils R-Biobase R-DBI R-RSQLite 

%description
Provides user interface and database connection code  for annotation 
data packages using SQLite data storage.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}

# noarch -> Architecture independent package
mkdir -p %{buildroot}%{_datadir}/R/library 
R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)

rm -rf %{buildroot}%{_datadir}/R/library/R.css

rm -f %{buildroot}%{_datadir}/R/library/AnnotationDbi/ProbePkg-template/data/.dummy.txt

%check
# Not performed, the list of metadata asked is too long and not mandatory
#%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/doc
%doc %{_datadir}/R/library/%{packname}/NEWS
%doc %{_datadir}/R/library/%{packname}/TODO
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/AnnDbPkg-templates
%{_datadir}/R/library/%{packname}/ProbePkg-template
%{_datadir}/R/library/%{packname}/DBschemas
%{_datadir}/R/library/%{packname}/extdata
%{_datadir}/R/library/%{packname}/NOTES-Herve


%changelog
* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> - 1.14.1-1%{dist}
- build new version needed by ArrayExpressHTS etc.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 1.12.0-1
- Update to version 1.12.0

* Sat Sep 11 2010 pingou <pingou@pingoured.fr> 1.10.2-1
- Update to version 1.10.2

* Tue May 11 2010 pingou <pingou@pingoured.fr> 1.10.1-1
- Update to version 1.10.1
- Fix url to a more stable form
- Fix R for latex
- Remove R post/postun

* Sat Mar 27 2010 pingou <pingou@pingoured.fr> 1.8.2-1
- Update to 1.8.2

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.8.1-1
- Update to 1.8.1
- Remove the %%post and %%postun
- Adapt %%files to the new R

* Sat Aug 01 2009 pingou <pingou@pingoured.fr> 1.6.1-1
- Update to 1.6.1

* Wed May 06 2009 pingou <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora
