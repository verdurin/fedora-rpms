#disable rpath error
%global QA_RPATHS=$[ 0x0001|0x0002 ]

#workaround rpath and strip problems
%define debug_package %{nil}
%define __spec_install_post /usr/lib/rpm/brp-compress

#It's a binary RPM so don't want requires or provides
%define _use_internal_dependency_generator 0
%define __find_provides %{nil}
%define __find_requires %{nil}

Name:           eman2-bin
Version:        2.02
Release:        1%{?dist}
Summary:        Single particle EM analysis

Group:          Applications/Engineering
License:        BSD/GPL
URL:            http://blake.bcm.tmc.edu/eman/eman2
Source0:        eman-linux-x86_64-gcc4-%{version}.tar.bz2
Source1:	eman2-bin.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

EMAN (Electron Microscopy ANalysis) is a scientific image processing
suite, aimed at improving the resolution and quality of single
particle reconstructions. At its foundation is a flexible C++ library
with complete Python bindings. Through the high level commands/GUI,
single particle reconstructions can be performed with minimal human
effort to subnanometer resolutions. EMAN is our most mature and
comprehensive software package and as a result is at the core of
software development at NCMI. We are currently prototyping a
grid-enabled version of this package.

%prep


%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/opt/
cd %{buildroot}/opt/
tar jxf %SOURCE0
chmod 755 EMAN2/bin/*

mkdir -p %{buildroot}/etc/profile.d
install -pm 644 %SOURCE1 %{buildroot}/etc/profile.d

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir /opt/EMAN2
/opt/EMAN2/*
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.*sh


%changelog
* Mon Jun 13 2011 Adam Huffman <bloch@verdurin.com> - 2.0.2-1
- new upstream release 2.0.2

* Tue Nov 16 2010 Adam Huffman <bloch@verdurin.com> - 2.0RC3-1
- initial version

