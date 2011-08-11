Name:           picard-tools
Version:        1.50
Release:        1%{?dist}
Summary:        Java utilities to manipulate SAM files

Group:          Applications/Engineering
License:        MIT
URL:            http://picard.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.zip
Source1:	%{name}-README.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

Requires:       java >= 1:1.6.0
Requires:	jpackage-utils

%description

Picard comprises Java-based command-line utilities that manipulate SAM
files, and a Java API (SAM-JDK) for creating new programs that read
and write SAM files. Both SAM text format and SAM binary (BAM) format
are supported.

%prep
%setup -q

mv ../snappy-java-1.0.3-rc3.jar .

cp %{SOURCE1} %{name}-%{version}

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_javadir}/%{name}

cp *.jar %{buildroot}%{_javadir}/%{name}

cp snappy-java-1.0.3-rc3.jar %{buildroot}%{_javadir}/%{name}

mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
cp %{SOURCE1} %{buildroot}/%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/%{name}-README.txt

%{_javadir}/%{name}/*

%changelog
* Thu Aug 11 2011 Adam Huffman <bloch@verdurin.com> - 1.50-1
- initial version

