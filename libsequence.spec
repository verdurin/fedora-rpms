# libsequence2.spec
#
# Copyright (c) 2002 Kevin Thornton k-thornton@uchicago.edu
#
%define name libsequence
%define version 1.7.3
%define release 2
%define manifest %{_builddir}/%{name}-%{version}-%{release}.manifest

# required items
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2
Group: Development/Libraries

BuildRequires: boost-devel
# optional items
#Vendor: Kevin Thornton
#Distribution:
#Icon:
#URL:
#Packager: Kevin Thornton k-thornton@uchicago.edu

# source + patches
Source: %{name}-%{version}.tar.gz
#Source1:
#Patch:
#Patch1:

# RPM info
#Provides:
#Requires:
#Conflicts:
#Prereq:

#Prefix: /usr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Summary: a library for various sequence I/O operations

%description
a library for various sequence I/O operations


%package      devel
Summary:      Development files for %{name}
Group:	      Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
#%patch0 -p1

%build
%configure
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

make install DESTDIR=%{buildroot}
rm %{buildroot}/%{_libdir}/%{name}.*a

%clean
rm -f %{manifest}
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog
%{_libdir}/%{name}*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/Sequence
%{_libdir}/%{name}*.so


%changelog
* Fri Sep  9 2011 Adam Huffman <bloch@verdurin.com> - 1.7.3-2
- -devel subpackage
- fix install 

* Thu Aug 18 2011 Adam Huffman <bloch@verdurin.com> - 1.7.3-1
- initial version, based on upstream template

