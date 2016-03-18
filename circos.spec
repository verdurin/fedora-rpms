Name:           circos
Version:        0.67
Release:        1%{?dist}
Summary:        

License:        GPLv2+
URL:            http://circos.ca
Source0:        

BuildArch:      
# Correct for lots of packages, other common choices include eg. Module::Build
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description


%prep
%setup -q


%build
# Remove OPTIMIZE=... from noarch packages (unneeded)
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc
# For noarch packages: vendorlib
%{perl_vendorlib}/*
# For arch-specific packages: vendorarch
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*.3*


%changelog
* Fri Mar 18 2016 Adam Huffman <bloch@verdurin.com>
- 
