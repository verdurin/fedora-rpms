%global		zipname	picard-tools

Name:		picard-tools-bin
Version:	1.50
Release:	2%{?dist}
Summary:	Java utilities to manipulate SAM files

Group:		Applications/Engineering
License:	MIT
URL:		http://picard.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{zipname}-%{version}.zip
Source1:	%{zipname}-README.txt
BuildRoot:	%{_tmppath}/%{zipname}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

Requires:	java >= 1:1.6.0
Requires:	jpackage-utils

%description

Picard comprises Java-based command-line utilities that manipulate SAM
files, and a Java API (SAM-JDK) for creating new programs that read
and write SAM files. Both SAM text format and SAM binary (BAM) format
are supported.

%prep
%setup -q -n %{zipname}-%{version}

mv ../snappy-java-1.0.3-rc3.jar .

cp %{SOURCE1} %{zipname}-%{version}

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_javadir}/%{zipname}

cp *.jar %{buildroot}%{_javadir}/%{zipname}

cp snappy-java-1.0.3-rc3.jar %{buildroot}%{_javadir}/%{zipname}

mkdir -p %{buildroot}/%{_docdir}/%{zipname}-%{version}
cp %{SOURCE1} %{buildroot}/%{_docdir}/%{zipname}-%{version}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_docdir}/%{zipname}-%{version}/%{zipname}-README.txt

%{_javadir}/%{zipname}/*

%changelog
* Tue Aug 23 2011 Adam Huffman <bloch@verdurin.com> - 1.50-2
- change to picard-tools-bin

* Thu Aug 11 2011 Adam Huffman <bloch@verdurin.com> - 1.50-1
- initial version

