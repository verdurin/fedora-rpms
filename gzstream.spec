Name:           gzstream
Version:	1.5
Release:        1%{?dist}
Summary:        zlib functions in C++ iostream

Group:          System Environment/Libraries
License:        LGPLv2.1+
URL:            http://www.cs.unc.edu/Research/compgeom/%{name}/
Source0:        http://www.cs.unc.edu/Research/compgeom/%{name}/%{name}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  zlib-devel

%description

Gzstream is a small C++ library, basically just a wrapper, that
provides the functionality of the zlib C-library in a C++ iostream.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n gzstream


%build
make default %{?_smp_mflags} CPPFLAGS="%{optflags}" -I.


%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
#find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
make test

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Thu Jun 30 2011 Adam Huffman <bloch@verdurin.com> - 1.5-1
- initial version

