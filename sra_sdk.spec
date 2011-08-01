%global preversion	rc1

Name:		sra_sdk
Version:	2.1.2
Release:	1%{?dist}
Summary:	NCBI SRA toolkit

Group:		Applications/Engineering
License:	Public Domain
URL:		http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=software
Source0:	http://trace.ncbi.nlm.nih.gov/Traces/sra/static/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	zlib-devel
BuildRequires:	libxml2-devel
BuildRequires:	bzip2-devel
BuildRequires:	libcurl-devel

%description

Toolkit for the Short Read Archive from NCBI

%prep
%setup -q -n %{name}-%{version}


%build
make OUTDIR="%{_builddir}/%{name}-%{version}" out
make dynamic
make


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
rm -rf %{_builddir}/linux/rel/gcc/%{_arch}/bin/ncbi 
chmod -R 0755 %{_builddir}/%{name}-%{version}/linux/rel/gcc/%{_arch}/bin
cp -a %{_builddir}/%{name}-%{version}/linux/rel/gcc/%{_arch}/bin/* %{buildroot}%{_bindir}
rm -rf %{_builddir}/linux/rel/gcc/%{_arch}/lib/ncbi 
chmod -R 0755 %{_builddir}/%{name}-%{version}/linux/rel/gcc/%{_arch}/lib
cp -a %{_builddir}/%{name}-%{version}/linux/rel/gcc/%{_arch}/lib/* %{buildroot}%{_libdir}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGES README USAGE
%{_bindir}/*
%{_libdir}/*



%changelog
* Mon Aug  1 2011 Adam Huffman <bloch@verdurin.com> - 2.1.2-1
- update to upstream 2.1.2 release
- add BR for libcurl-devel
- includes changes to fastq-dump behaviour - see README

* Fri Jul 15 2011 Adam Huffman <bloch@verdurin.com> - 2.1.0-1
- update to 2.1.0

* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> - 2.0.1-0.1.rc1%{?dist}
- initial version



