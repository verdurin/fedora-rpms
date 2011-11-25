%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:		pybedtools
Version:	0.5.5
Release:	1%{?dist}
Summary:	Wrapper around BEDTools for bioinformatics work

Group:		Applications/Engineering
License:	GPLv2+
URL:		http://packages.python.org/pybedtools/
Source0:	http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:	python-argparse
BuildRequires:	python-sphinx
BuildRequires:	zlib-devel

%description
pybedtools is a Python extension of Aaron Quinlan's BEDtools suite
(http://code.google.com/p/bedtools/), used for comparing genomic
features.

pybedtools allows you to intuitively call BEDtools programs from
within Python without writing awkward system calls, and allows you to
manipulate data on the file level as well as on the individual feature
level.

%prep
%setup -q


%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="%{optflags}" %{__python} setup.py build

#cd docs
#make html
#TODO: make PDF docs, requiring LaTeX

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.rst 
# For arch-specific packages: sitearch
%{python_sitearch}/*
%{_bindir}/*.py*

%changelog
* Fri Nov 25 2011 Adam Huffman <verdurin@fedoraproject.org> - 0.5.5-1
- initial version

