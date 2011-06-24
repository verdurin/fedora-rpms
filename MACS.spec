# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}


Name:           MACS
Version:        1.4.0
Release:        0.1.rc2%{?dist}
Summary:        Model-based Analysis for ChIP-Seq

Group:          Development/Languages
License:        Artistic 2.0
URL:            http://liulab.dfci.harvard.edu/MACS/index.html
Source0:        http://liulab.dfci.harvard.edu/MACS/src/MACS-1.4.0rc2.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel

%description

Next generation parallel sequencing technologies made chromatin
immunoprecipitation followed by sequencing (ChIP-Seq) a popular
strategy to study genome-wide protein-DNA interactions, while creating
challenges for analysis algorithms. We present Model-based Analysis of
ChIP-Seq (MACS) on short reads sequencers such as Genome Analyzer
(Illumina / Solexa). MACS empirically models the length of the
sequenced ChIP fragments, which tends to be shorter than sonication or
library construction size estimates, and uses it to improve the
spatial resolution of predicted binding sites. MACS also uses a
dynamic Poisson distribution to effectively capture local biases in
the genome sequence, allowing for more sensitive and robust
prediction. MACS compares favorably to existing ChIP-Seq peak-finding
algorithms, is publicly available open source, and can be used for
ChIP-Seq with or without control samples.

%prep
%setup -q -n MACS-1.4.0rc2


%build
%{__python} setup.py build

%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot}
 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc 00README ChangeLog COPYING
%{python_sitelib}/*
%{_bindir}/macs14
%{_bindir}/eland*
%{_bindir}/sam2bed
%{_bindir}/wignorm

%changelog
* Thu Apr 21 2011 Adam Huffman <bloch@verdurin.com> - 1.4.0-0.1.rc2
- new upstream release
- new binary names

* Thu Dec 16 2010 Adam Huffman <bloch@verdurin.com> - 1.4.0beta-1
- initial version

