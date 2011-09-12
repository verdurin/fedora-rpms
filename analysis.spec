Name:           analysis
Version:        0.8.0
Release:        1%{?dist}
Summary:        Evolutionary genetic analysis tools

License:	GPLv2+
URL:		http://molpopgen.org/software/analysis/
Source0:	http://molpopgen.org/software/analysis/analysis-0.8.0.tar.gz

BuildRequires:  libsequence
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
%doc



%changelog
* Fri Sep  9 2011 Adam Huffman <bloch@verdurin.com> - 0.8.0-1
- Initial version

