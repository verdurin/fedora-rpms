# libsequence2.spec
#
# Copyright (c) 2002 Kevin Thornton k-thornton@uchicago.edu
#
%define name libsequence
%define version 1.7.3
%define release 1
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


%prep
%setup -q
#%patch0 -p1

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
%makeinstall

# __os_install_post is implicitly expanded after the
# %_install section... do it now, and then disable it,
# so all work is done before building manifest.

%{?__os_install_post}
%define __os_install_post %{nil}

# build the file list automagically into %{manifest}

cd $RPM_BUILD_ROOT
rm -f %{manifest}
find . -type d \
        | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' >> %{manifest}
find . -type f \
        | sed 's,^\.,\%attr(-\,root\,root) ,' >> %{manifest}
find . -type l \
        | sed 's,^\.,\%attr(-\,root\,root) ,' >> %{manifest}

#%pre
#%post
#%preun
#%postun

%clean
rm -f %{manifest}
rm -rf $RPM_BUILD_ROOT

%files -f %{manifest}
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog
#%docdir
#%config

%changelog
* Thu Aug 18 2011 Adam Huffman <bloch@verdurin.com> - 1.7.3-1
- initial version, based on upstream template

