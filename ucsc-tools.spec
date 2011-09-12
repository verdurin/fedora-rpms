%global MYSQLLIBS "%{_libdir}/mysql/libmysqlclient.so -lz"
%global MYSQLINC "%{_includedir}/mysql"

%global CGI_BIN	 "%{_builddir}/var/www/cgi-bin"
%global	DOCUMENTROOT	"%{_builddir}/var/www/html"
%global SCRIPTS		"%{_builddir}/%{_bindir}"

Name:           ucsc-tools
Version:        248
Release:        6%{?dist}
Summary:        Various useful bioinformatics tools from UCSC

Group:          Applications/Engineering
License:        GPLv2
URL:            http://genomewiki.ucsc.edu/index.php/Main_Page
Source0:        jksrc.v%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  mysql-devel libpng-devel zlib-devel rsync

%description

Various programs from the UCSC Genome team

%package          browser
Summary:          UCSC Browser
Group:            Applications/Engineering
Requires:         %{name} = %{version}

%description browser

Files needed for a local UCSC Genome Browser installation


%prep
%setup -q -n kent


# Filter unwanted Requires:
mkdir %{_builddir}/%{name}-%{version}
cat << \EOF > %{_builddir}/%{name}-%{version}/%{name}-req
#!/bin/sh
%{__perl_requires} $* |\
  sed -e '/perl(the)$/d'
EOF

%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build
cd src

# Ugly fix for bad CGI_BIN Paths
# fix up paths in build tree makefiles
find . -name makefile -exec \
sed -i 's/\${CGI_BIN}-\${USER}/\${CGI_BIN}/g' {} \;

find . -name makefile -exec \
sed -i 's/\${DESTDIR}\${CGI_BIN}/\${CGI_BIN}/g' {} \;

find . -name *.mk -exec \
sed -i 's/\${CGI_BIN}-\${USER}/\${CGI_BIN}/g' {} \;

# Picky about format of MACHTYPE value
%ifarch x86_64
%global MACHTYPE x86_64
%endif

%ifarch i386 i586 i686
%global MACHTYPE i386
%endif

mkdir -p %{_builddir}/%{_bindir}

# Workaround hardcoded Apache location
mkdir -p %{_builddir}/%{_localstatedir}/www/html
mkdir -p %{_builddir}/%{_localstatedir}/www/cgi-bin


# Need to define mysql variables
make %{?_smp_mflags} MYSQLLIBS=%{MYSQLLIBS} MYSQLINC=%{MYSQLINC} \
MACHTYPE=%{MACHTYPE} DESTDIR=%{_builddir} BINDIR=%{_builddir}/%{_bindir} \
CGI_BIN=%{CGI_BIN} DOCUMENTROOT=%{DOCUMENTROOT} SCRIPTS=%{SCRIPTS}


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_localstatedir}/www/cgi-bin
mkdir -p %{buildroot}/%{_localstatedir}/www/html/js

#rm -rf %{_builddir}/var/www/html
#rm -rf %{_builddir}/var/www/cgi-bin

install -m 0755 %{_builddir}/var/www/html/js/*/*.js %{buildroot}/%{_localstatedir}/www/html/js/
#rm -rf %{_builddir}/var/www/html/js
#install -m 0755 %{_builddir}/var/www/html/* %{buildroot}/%{_localstatedir}/www/html

install -d -m 0755 %{_builddir}/var/www/cgi-bin/greatData %{buildroot}/%{_localstatedir}/www/cgi-bin
rm -rf %{_builddir}/var/www/cgi-bin/greatData
install -d -m 0755 %{_builddir}/var/www/cgi-bin/hgcData %{buildroot}/%{_localstatedir}/www/cgi-bin
rm -rf %{_builddir}/var/www/cgi-bin/hgcData
install -d -m 0755 %{_builddir}/var/www/cgi-bin/hgCgiData %{buildroot}/%{_localstatedir}/www/cgi-bin
rm -rf %{_builddir}/var/www/cgi-bin/hgCgiData
install -d -m 0755 %{_builddir}/var/www/cgi-bin/hgGeneData %{buildroot}/%{_localstatedir}/www/cgi-bin
rm -rf %{_builddir}/var/www/cgi-bin/hgGeneData
install -d -m 0755 %{_builddir}/var/www/cgi-bin/hgNearData %{buildroot}/%{_localstatedir}/www/cgi-bin
rm -rf %{_builddir}/var/www/cgi-bin/hgNearData
install -d -m 0755 %{_builddir}/var/www/cgi-bin/loader %{buildroot}/%{_localstatedir}/www/cgi-bin
rm -rf %{_builddir}/var/www/cgi-bin/loader

install -m 0755 %{_builddir}/var/www/cgi-bin/* %{buildroot}/%{_localstatedir}/www/cgi-bin

install -m 0755 %{_builddir}%{_bindir}/* %{buildroot}/%{_bindir}

# super-ugly hack until all build paths fixed
install -m 0755 %{_builddir}%{_builddir}%{_bindir}/* %{buildroot}/%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc src/README src/CHANGES

%{_bindir}/*

%files browser
%defattr(-,root,root,-)

%{_localstatedir}/www/cgi-bin/*
%{_localstatedir}/www/html/*

%changelog
* Tue Apr  5 2011 Adam Huffman <bloch@verdurin.com> - 248-6
- subpackage for browser files

* Fri Mar 18 2011 Adam Huffman <bloch@verdurin.com> - 248-5
- filter incorrect Perl requires, thanks to Marcela Maslanova in #fedora-perl

* Thu Mar 17 2011 Adam Huffman <bloch@verdurin.com> - 248-4
- weird location for hg/utils/*

* Wed Mar 16 2011 Adam Huffman <bloch@verdurin.com> - 248-3
- workarounds for lack of separate 'make install'
- remove unwanted /var/www/html/js and /var/www/cgi-bin

* Wed Mar 16 2011 Adam Huffman <bloch@verdurin.com> - 248-2
- better fixes for path problems
- some makefiles use destdir, some don't...

* Fri Mar 11 2011 Adam Huffman <bloch@verdurin.com> - 248-1
- initial version

