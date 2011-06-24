Name:		filo
Version:	1.1.0
Release:	2%{?dist}
Summary:	Useful FILe and stream Operations

Group:		Applications/Engineering
License:	GPLv2
URL:		https://github.com/arq5x/filo
#correct as of 2011-06-24
Source0:	https://github.com/arq5x/filo/tarball/master/arq5x-filo-f56efe3.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	zlib-devel

%description 
Filo consists of various useful file and stream operations, including
some that were originally part of BEDTools.

%prep
%setup -q -n arq5x-filo-f56efe3

#fix spurious permissions
chmod 0644 src/shuffle/shuffle.cpp
chmod 0644 src/stats/stats.cpp

%build
make %{?_smp_mflags} CXXFLAGS="-I. %{optflags}"


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 bin/* %{buildroot}/%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.rst
%{_bindir}/groupBy
%{_bindir}/shuffle
%{_bindir}/stats

%changelog
* Fri Jun 24 2011 Adam Huffman <bloch@verdurin.com> - 1.1.0-2
- previous patch upstreamed
- fix bad permissions on shuffle.cpp

* Fri Feb 18 2011 Adam Huffman <bloch@verdurin.com> - 1.1.0-1
- initial version
- patch to fix missing includes
