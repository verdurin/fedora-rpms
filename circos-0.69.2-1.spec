Name:           circos
Version:        0.69-2
Release:        1%{?dist}
Summary:        Data and information visualization with a circular layout

License:        GPLv2+
URL:            http://circos.ca
Source0:        http://circos.ca/distribution/circos-0.69-2.tgz

BuildArch:      
# Correct for lots of packages, other common choices include eg. Module::Build
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description

Circos is a software package for visualizing data and information. It
visualizes data in a circular layout — this makes Circos ideal for exploring
relationships between objects or positions. There are other reasons why a
circular layout is advantageous, not the least being the fact that it is
attractive.

Circos is ideal for creating publication-quality infographics and illustrations
with a high data-to-ink ratio, richly layered data and pleasant symmetries. You
have fine control each element in the figure to tailor its focus points and
detail to your audience.

%prep
%setup -q -n circos-0.69-2


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



%install
mkdir -p %{buildroot}%{installroot}
cp -r bin data error etc example fonts lib tiles %{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/data/karyotype/parse.karyotype
%{installroot}/data/karyotype/assembly/parse.assembly
%{installroot}/example/run
