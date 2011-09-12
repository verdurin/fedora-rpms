# libsequence2.spec
#
# Copyright (c) 2002 Kevin Thornton k-thornton@uchicago.edu
#
Name:		libsequence
Version:	1.7.3
Release:	3%{?dist}
Summary:	Genomics and evolutionary genetics library

License:	GPLv2
URL:		http://molpopgen.org/software/%{name}.html
Source0:	http://molpopgen.org/software/%{name}/%{name}-%{version}.tar.gz

Group:		Development/Libraries

BuildRequires:	boost-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



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

%build
%configure
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

make install DESTDIR=%{buildroot}
rm %{buildroot}/%{_libdir}/%{name}.*a

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog
%{_libdir}/%{name}*.so.*

%files devel
%defattr(-,root,root)
%doc doc examples
%{_includedir}/Sequence
%{_libdir}/%{name}*.so


%changelog
* Mon Sep 12 2011 Adam Huffman <bloch@verdurin.com> - 1.7.3-3
- remove unnecessary upstream spec cruft

* Fri Sep  9 2011 Adam Huffman <bloch@verdurin.com> - 1.7.3-2
- -devel subpackage
- fix install 

* Thu Aug 18 2011 Adam Huffman <bloch@verdurin.com> - 1.7.3-1
- initial version, based on upstream template

