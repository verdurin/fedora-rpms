%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           EMAN2
Version:        2.02
Release:        2%{?dist}
Summary:        Single particle EM analysis

Group:          Applications/Engineering
License:        BSD and GPL
URL:            http://blake.bcm.tmc.edu/eman/eman2
Source0:        eman-source-%{version}.tar.gz
Source1:	EMAN2.sh
Patch0:		eman2-boost-include.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cmake zlib-devel python-devel libpng-devel fftw3-devel
BuildRequires:	hdf5-devel gsl-devel libtiff-devel libjpeg-devel

%if 0%{?rhel}
BuildRequires:	boost141-devel qt4-devel
Requires:	boost141
%else
BuildRequires:	boost-devel qt-devel
%endif

BuildRequires:	numpy

Requires:	ipython

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
#make VERBOSE=1 %{?_smp_mflags} DESTDIR=%{buildroot}
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
mkdir -p %{buildroot}%{_datadir}/%{name}/test
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}/%{python_sitearch}/%{name}
mkdir -p %{buildroot}/%{python_sitearch}/%{name}/pyemtbx

# separate files installed in single hierarchy
#mkdir -p %{buildroot}%{_bindir}
#mkdir -p %{buildroot}%{_libdir}/
#mkdir -p %{buildroot}%{_datadir}/examples
#mkdir -p %{buildroot}opt/%{_datadir}/%{name}/images
#mkdir -p %{buildroot}opt/%{_includedir}/%{name}
#mkdir -p %{buildroot}opt/%{_docdir}/%{name}


install  -m 0755 %{buildroot}/builddir/EMAN2/bin/* %{buildroot}%{_bindir}

cp -dpr %{buildroot}/builddir/EMAN2/include/* %{buildroot}%{_includedir}/%{name}

install -m 0755 %{buildroot}/builddir/EMAN2/examples/* %{buildroot}%{_datadir}/%{name}/examples/

cp -dpr %{buildroot}/builddir/EMAN2/test/* %{buildroot}%{_datadir}/%{name}/test
cp -dpr %{buildroot}/builddir/EMAN2/images/* %{buildroot}%{_datadir}/%{name}/images/

cp -dpr %{buildroot}/builddir/EMAN2/doc %{buildroot}%{_defaultdocdir}/%{name}-%{version}/ 

cp -dpr %{buildroot}/builddir/EMAN2/lib/*.py* %{buildroot}/%{python_sitearch}/%{name}
cp -dpr %{buildroot}/builddir/EMAN2/lib/pyemtbx/* %{buildroot}/%{python_sitearch}/%{name}/pyemtbx/
cp -dpr %{buildroot}/builddir/EMAN2/lib/lib*.so %{buildroot}/%{python_sitearch}/%{name}
cp -dpr %{buildroot}/builddir/EMAN2/lib/libEM2.so %{buildroot}%{_libdir}/
cp -dpr %{buildroot}/builddir/EMAN2/lib/libGLEM2.so %{buildroot}%{_libdir}/

#chmod 0755 %{buildroot}%{_libdir}

mkdir -p %{buildroot}/etc/profile.d
install -pm 644 %SOURCE1 %{buildroot}/etc/profile.d

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
%{_datadir}/%{name}/test
%{_docdir}/%{name}-%{version}/
%{python_sitearch}/%{name}/*
%{_libdir}/libEM2.so
%{_libdir}/libGLEM2.so
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}/


%changelog
* Fri Jun 24 2011 Adam Huffman <bloch@verdurin.com> - 2.02-2
- fix bad source file permissions
- add script to set EMAN2DIR variable
- add reqs. for ipython
- fix layout

* Mon Jun 20 2011 Adam Huffman <bloch@verdurin.com> - 2.02-2
- use upstream single directory layout

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

