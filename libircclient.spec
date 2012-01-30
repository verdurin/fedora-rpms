Name:		libircclient
Version:	1.5
Release:	1%{?dist}
Summary:	Library implementing client-server IRC protocol
Group:		System Environment/Libraries
License:	LGPLv2+
URL:		http://%{name}.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
#Patch obsolete because upstream buildsystem ignored now
#Patch0:		%%{name}-makefile.patch
#Attempted fix for GCC 4.4+ strict aliasing problems
#Patch0:		%{name}-strictaliasing.patch
#Patch1:		%{name}-strictaliasing-dcc.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


BuildRequires:	automake

%description
It is designed to be small, fast, portable and compatible to RFC standards,
and most IRC clients. libircclient features include:
  * Full multi-threading support.
  * Single threads handles all the IRC processing.
  * Support for single-threaded applications, and socket-based
    applications, which use select()
  * Synchronous and asynchronous interfaces.
  * CTCP support with optional build-in reply code.
  * Flexible DCC support, including both DCC chat, and DCC file transfer.
  * Can both initiate and react to initiated DCC.
  * Can accept or decline DCC sessions asynchronously.
  * Plain C interface and implementation (possible to use from C++ code,
    obviously)
  * Compatible with RFC 1459 and most IRC clients.
  * Free, licensed under LGPL license.
  * Good documentation and examples available.

%package devel
Summary: Header files and libraries for compiling against %{name}
Group:	 Development/System
Requires: %name = %version-%release

%description devel

Header files for compiling against %{name}

%prep
%setup -q
#%%patch0
#%patch0 -p1 -b .%{name}-strictaliasing.patch
#%patch1 -p1 -b .%{name}-strictaliasing-dcc.patch

%build
#autoreconf
%configure --enable-ipv6

cd src
gcc %{optflags} -fPIC -I../include -c libircclient.c
ar rc libircclient-%{version}.a libircclient.o
gcc -shared -Wl,-soname,libircclient.so.1 libircclient.o -o libircclient.so.1

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_mandir}/man3
cd src

install -m 0755 libircclient.so.1 %{buildroot}%{_libdir}/
cd %{buildroot}%{_libdir}
ln -s libircclient.so.1 libircclient.so

cd -
cd ../include
for hdr in libirc*.h ; do
    install -m 644 "$hdr" %{buildroot}%{_includedir}/
done
cd ../doc
for mp in man/man3/*.3 ; do
    install -m 644 "$mp" %{buildroot}%{_mandir}/man3/
done



%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc Changelog LICENSE README THANKS 
%{_libdir}/libircclient.so.*
%{_mandir}/man3/*

%files devel
%defattr(-,root,root,-)
%doc doc/html examples
%{_includedir}/*
%{_libdir}/libircclient.so


%changelog
* Fri Jan 20 2012 Adam Huffman <verdurin@fedoraproject.org> - 1.5-1
- New upstream release 1.5
- disable GCC 4.7 patches for now

* Wed Jan 11 2012 Adam Huffman <verdurin@fedoraproject.org> - 1.3-8
- two patches to fix strict aliasing problems

* Sun Jan  8 2012 Adam Huffman <verdurin@fedoraproject.org> - 1.3-7
- complete removal of upstream buildsystem
- more consistent use of macros

* Mon May  2 2011 Adam Huffman <bloch@verdurin.com> - 1.3-6
- better soname fix

* Fri Apr 29 2011 Adam Huffman <bloch@verdurin.com> - 1.3-5
- fix soname

* Fri Apr 29 2011 Adam Huffman <bloch@verdurin.com> - 1.3-4
- ignore provided makefiles
- devel subpackage

* Fri Apr 29 2011 Adam Huffman <bloch@verdurin.com> - 1.3-3
- remove static library

* Sat Feb 12 2011 Adam Huffman <bloch@verdurin.com> - 1.3-2
- fixes taken from Arch package to help with din
- build .so

* Wed Jun 2 2010 Conrad Meyer <konrad@tylerc.org> - 1.3-1
- First attempt at a package (crappy)
