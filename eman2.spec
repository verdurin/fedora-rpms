Name:           eman2
Version:        2.02
Release:        1%{?dist}
Summary:        Single particle EM analysis

Group:          Applications/Engineering
License:        BSD and GPL
URL:            http://blake.bcm.tmc.edu/eman/eman2
Source0:        eman-source-%{version}.tar.gz
Patch0:		eman2-boost-include.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cmake zlib-devel python-devel libpng-devel fftw3-devel
BuildRequires:	hdf5-devel gsl-devel libtiff-devel libjpeg-devel

BuildRequires: qt-devel boost141-devel

BuildRequires:	numpy

%description

EMAN2 is the successor to EMAN1. It is a broadly based greyscale
scientific image processing suite with a primary focus on processing
data from transmission electron microscopes. EMAN's original purpose
was performing single particle reconstructions (3-D volumetric models
from 2-D cryo-EM images) at the highest possible resolution, but the
suite now also offers support for single particle cryo-ET, and tools
useful in many other subdisciplines such as helical reconstruction,
2-D crystallography and whole-cell tomography. Image processing in a
suite like EMAN differs from consumer image processing packages like
Photoshop in that pixels in images are represented as floating-point
numbers rather than small (8-16 bit) integers. In addition, image
compression is avoided entirely, and there is a focus on quantitative
analysis rather than qualitative image display.

%package       devel
Summary:       Development files for %{name}
Group:	       Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n EMAN2

#Use boost141 headers on EPEL5
%if 0%{?rhel}
%patch0 -p1 -b .boost-include.patch
%endif

%build

cd src/build
%cmake ../eman2 
make VERBOSE=1 %{?_smp_mflags} DESTDIR=%{buildroot}


%install
rm -rf %{buildroot}
cd src/build
make install DESTDIR=%{buildroot}

# separate files installed in single hierarchy
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
mkdir -p %{buildroot}%{_datadir}/%{name}/images
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}

install  -m 0755 %{buildroot}/builddir/EMAN2/bin/* %{buildroot}%{_bindir}

cp -dpr %{buildroot}/builddir/EMAN2/include/* %{buildroot}%{_includedir}/%{name}

install -m 0755 %{buildroot}/builddir/EMAN2/examples/* %{buildroot}%{_datadir}/%{name}/examples/

cp -dpr %{buildroot}/builddir/EMAN2/images/* %{buildroot}%{_datadir}/%{name}/images/

cp -dpr %{buildroot}/builddir/EMAN2/doc %{buildroot}%{_defaultdocdir}/%{name}-%{version}/ 

cp -dpr %{buildroot}/builddir/EMAN2/lib/* %{buildroot}%{_libdir}/%{name}
chmod 0755 %{buildroot}%{_libdir}/%{name}

rm -rf %{buildroot}/builddir/EMAN2



%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%dir %{_docdir}/%{name}
%{_bindir}/*.py*
%{_bindir}/e2speedtest
%{_bindir}/sparx
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/images
%{_docdir}/%{name}-%{version}/
%{_libdir}/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}/


%changelog
* Fri Jun 17 2011 Adam Huffman <bloch@verdurin.com> - 2.02-1
- new upstream release 2.02
- add patch for boost141 headers on EPEL5
- use boost141 on EPEL5

* Mon Jun 13 2011 Adam Huffman <bloch@verdurin.com> - 2.01-1
- new upstream release 2.01

* Tue Nov 16 2010 Adam Huffman <bloch@verdurin.com> - 2.0RC3-3
- various files/install fixes

* Wed Nov  3 2010 Adam Huffman <bloch@verdurin.com> - 2.0RC3-2
- use qt-devel for EPEL

* Mon Oct 18 2010 Adam Huffman <bloch@verdurin.com> - 2.0RC3-1
- new upstream version
- fix docs

* Thu Jun 24 2010 Adam Huffman <bloch@verdurin.com> - 2.0rc2-1
- new upstream version

* Tue Mar 23 2010 Adam Huffman <bloch@verdurin.com> - 1-1
- initial version

