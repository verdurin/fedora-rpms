%global preversion	rc1

Name:           sra_sdk
Version:        2.0.1
Release:        0.1.%{rc}%{?dist}
Summary:        NCBI SRA toolkit

Group:          Applications/Engineering
License:        Public Domain
URL:            http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=software
Source0:        http://trace.ncbi.nlm.nih.gov/Traces/sra/static/sra_sdk-2.0.1rc1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	zlib-devel libxml2-devel bzip2-devel

%description

Toolkit for the Short Read Archive from NCBI

%prep
%setup -q -n %{name}-%{version}%{preversion}


%build
make OUTDIR="%{_builddir}/%{name}-%{version}" out
make dynamic
make


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
rm -rf %{_builddir}/linux/rel/gcc/%{_arch}/bin/ncbi 
chmod -R 0755 %{_builddir}/%{name}-%{version}%{preversion}/linux/rel/gcc/%{_arch}/bin
cp -a %{_builddir}/%{name}-%{version}%{preversion}/linux/rel/gcc/%{_arch}/bin/* %{buildroot}%{_bindir}
rm -rf %{_builddir}/linux/rel/gcc/%{_arch}/lib/ncbi 
chmod -R 0755 %{_builddir}/%{name}-%{version}%{preversion}/linux/rel/gcc/%{_arch}/lib
cp -a %{_builddir}/%{name}-%{version}%{preversiona}/linux/rel/gcc/%{_arch}/lib/* %{buildroot}%{_libdir}

%clean
#rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGES README USAGE
%{_bindir}/*
%{_libdir}/*



%changelog
* Wed Apr 20 2011 Adam Huffman <bloch@verdurin.com> - 2.0.1rc1-1
- initial version

