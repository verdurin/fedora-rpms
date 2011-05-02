Name:		tabix
Version:	0.2.5
Release:	1%{?dist}
Summary:	Generic indexer for TAB-delimited genome position files

Group:		Applications/Engineering
License:	MIT
URL:		http://samtools.sourceforge.net/tabix.shtml
Source0:	http://download.sourceforge.net/samtools/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	zlib-devel
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Simple)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Tabix indexes a TAB-delimited genome position file in.tab.bgz and
creates an index file in.tab.bgz.tbi when region is absent from the
command-line. The input data file must be position sorted and
compressed by bgzip which has a gzip(1) like interface. After
indexing, tabix is able to quickly retrieve data lines overlapping
regions specified in the format "chr:beginPos-endPos". Fast data
retrieval also works over network if URI is given as a file name and
in this case the index file will be downloaded if it is not present
locally.

%prep
%setup -q


%build
make %{?_smp_mflags}

# Perl module not built by default - in separate subdir.
cd perl
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

install -m 0755 bgzip %{buildroot}%{_bindir}
install -m 0755 tabix %{buildroot}%{_bindir}
install -m 0755 tabix.py %{buildroot}%{_bindir}
install -m 0644 tabix.1 %{buildroot}%{_mandir}/man1

cd perl
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*
rm %{buildroot}%{perl_vendorarch}/auto/Tabix/Tabix.bs

%check
cd perl
make test

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc NEWS ChangeLog example.gtf.gz example.gtf.gz.tbi TabixReader.java 

%{_bindir}/bgzip
%{_bindir}/tabix
%{_bindir}/tabix.py

%{_mandir}/man1/tabix.1*

%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/


%changelog
* Mon May  2 2011 Adam Huffman <bloch@verdurin.com> - 0.2.5-1
- new upstream version

* Tue Apr 19 2011 Adam Huffman <bloch@verdurin.com> - 0.2.4-1
- new upstream release

* Tue Mar 22 2011 Adam Huffman <bloch@verdurin.com> - 0.2.3-1
- initial version
- include perl code not compiled by default
- remove static library
- remove Tabix.bs
- Java example in docs
