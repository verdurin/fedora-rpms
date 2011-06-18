Name:		Send2Trash3k
Version:	1.2.0
Release:	1%{?dist}
Summary:	Send files to trash across platforms

Group:		Development/Languages
License:	Redistributable, no modification permitted
URL:		http://pypi.python.org/pypi/Send2Trash3k
Source0:	http://pypi.python.org/packages/source/S/Send2Trash3k/Send2Trash3k-1.2.0.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%description
Send2Trash is a small package that sends files to the Trash (or
Recycle Bin) *natively* and on *all platforms*. On OS X, it uses
native ``FSMoveObjectToTrashSync`` Cocoa calls, on Windows, it uses
native (and ugly) ``SHFileOperation`` win32 calls. On other platforms,
it follows the trash specifications from freedesktop.org.

%prep
%setup -q


%build
%{__python3} setup.py build


%install
rm -rf %{buildroot}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README CHANGES
# For noarch packages: sitelib
%{python3_sitelib}/*



%changelog
* Fri Jun 17 2011 Adam Huffman <bloch@verdurin.com> - 1.2.0-1
- Initial version

