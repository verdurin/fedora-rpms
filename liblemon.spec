%global		realname	lemon

Name:		liblemon
Version:	1.2.2
Release:	1%{?dist}
Summary:	Library of Efficient Models and Optimization in Networks

Group:		Applications/Engineering
License:	Boost
URL:		http://lemon.cs.elte.hu/
Source0:	http://lemon.cs.elte.hu/pub/sources/%{realname}-%{version}.tar.gz
#Patch0:		%{name}-rpath.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	glpk-devel
BuildRequires:	automake

%description
LEMON stands for Library for Efficient Modeling and Optimization in
Networks.  It is a C++ template library providing efficient
implementations of common data structures and algorithms with focus on
combinatorial optimization tasks connected mainly with graphs and
networks.

LEMON is a member of the COIN-OR initiative, a collection of OR related
open source projects. You are free to use it in your commercial or
non-commercial applications under very permissive license terms.

The project was launched by the Egerváry Research Group on Combinatorial
Optimization (EGRES) at the Operations Research Department of the Eötvös
Loránd University, Budapest in 2003. Up to this point, the developers of
the library work at the Eötvös Loránd University, Budapest and at the
Budapest University of Technology and Economics.

%package 	    devel
Summary:	    Development files for %{name}
Group:		    Development/Libraries
Requires:	    %{name} = %{version}-%{release}
BuildRequires:	    pkgconfig

%description	    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{realname}-%{version}

#%patch0 -p1 -b .%{name}-rpath.patch

%build
#autoreconf
%configure --enable-shared --disable-static --disable-rpath
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

#remove libtool archive file
rm %{buildroot}/%{_libdir}/libemon.la

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README NEWS INSTALL LICENSE AUTHORS doc/
%{_bindir}/*
%{_libdir}/libemon*.so.*

%files	devel
%defattr(-,root,root)
%{_includedir}/lemon
%{_libdir}/pkgconfig/lemon.pc
%{_libdir}/libemon.so


%changelog
* Thu Sep 15 2011 Adam Huffman <bloch@verdurin.com> - 1.2.2-1
- initial version, based on OpenSuSE package

