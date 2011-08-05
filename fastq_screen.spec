Name:		fastq_screen
Version:	0.2.1
Release:	1%{?dist}
Summary:	Contamination screening for next-gen sequence data

Group:		Applications/Engineering
License:	GPLv3+
URL:		http://www.bioinformatics.bbsrc.ac.uk/projects/%{name}/
Source0:	http://www.bioinformatics.bbsrc.ac.uk/projects/%{name}/%{name}_v%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

Requires:	bowtie

%description

FastQ Screen provides a simple way to screen a library of short reads
against a set of reference libraries. Its most common use is as part
of a QC pipeline to confirm that a library comes from the expected
source, and to help identify any sources of contamination.

%prep
%setup -q -n %{name}_v%{version}


%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.txt RELEASE_NOTES.txt
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}


%changelog
* Fri Aug  5 2011 Adam Huffman <bloch@verdurin.com> - 0.2.1-1
- initial version

