Name:           analysis
Version:        0.8.0
Release:        2%{?dist}
Summary:        Evolutionary genetic analysis tools

Group:		Applications/Engineering
License:	GPLv2+
URL:		http://molpopgen.org/software/%{name}/
Source0:	http://molpopgen.org/software/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  libsequence-devel
BuildRequires:	gsl-devel


%description

A set of c++ programs for evolutionary genetic analysis.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc README AUTHORS ChangeLog COPYING
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Mon Sep 12 2011 Adam Huffman <bloch@verdurin.com> - 0.8.0-2
- add missing group field

* Fri Sep  9 2011 Adam Huffman <bloch@verdurin.com> - 0.8.0-1
- Initial version

