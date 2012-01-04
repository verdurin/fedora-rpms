%define debug_package %{nil}

#It's a binary RPM so don't want requires or provides
%define _use_internal_dependency_generator 0
%define __find_provides %{nil}
%define __find_requires %{nil}


Name:           sratoolkit
Version:        2.1.8
Release:        1%{?dist}
Summary:        Binary distribution of Short Read Archive toolkit

Group:          Applications/Engineering
License:        Public Domain
URL:            http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=show&f=software&m=software&s=software
Source0:        %{name}.%{version}-centos_linux64.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description

Various tools for working with Short Read Archive files, including
conversion tools to other formats

%prep

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
mkdir -p %{buildroot}%{_bindir}
cd %{buildroot}
tar zxf %SOURCE0

cd %{name}.%{version}-centos_linux64
mv README help/ %{buildroot}%{_docdir}/%{name}-%{version}
mv * %{buildroot}%{_bindir}
cd ..
rm -rf %{name}.%{version}-centos_linux64

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}/README
%doc %{_docdir}/%{name}-%{version}/help

%{_bindir}*

%changelog
* Wed Dec 14 2011 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.1.8-1
- Updated sratoolkit to version 2.1.8

* Tue Aug  2 2011 Adam Huffman <bloch@verdurin.com> - 2.1.2-1
- initial version

