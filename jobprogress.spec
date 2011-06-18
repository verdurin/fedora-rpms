# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}


Name:		    jobprogress
Version:	    1.0.1
Release:	    1%{?dist}
Summary:	    Cross-toolkit task progression reporting for GUIs

Group:		    Development/Languages
License:	    Redistributable, no modification permitted
URL:		    http://hg.hardcoded.net/jobprogress
#Source0:	    http://hg.hardcoded.net/jobprogress/get/1.0.1.tar.bz2
Source0:	    hsoft-jobprogress-66056f6d1e00.tar.bz2
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	    noarch
BuildRequires:	    python3-devel
BuildRequires:	    python3-setuptools

%description

When doing complex processing that has to report progress indication
to the user, things can get complex quick. Often, we don't know
beforehand how many work unit our processing will have, because
knowing it depends on another work unit for which the progress should
also be reported to the user. One example of such situation is
processing files after having collected them. When we start the
process, we don't know how many files we'll collect, so it's hard to
set a maximum value on our progress bar. ``jobprogress`` handles that.

Also, most of the time, we want to run our task in a separate thread
so the GUI stays smooth. ``jobprogress`` takes care of synchronizing
the threaded task and the GUI.

For now, only PyQt is supported, but the toolkit specific layer is
pretty thin, so it should be easy to add new toolkits.

%prep
%setup -q -n hsoft-jobprogress-66056f6d1e00


%build
%{__python3} setup.py build


%install
rm -rf %{buildroot}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE README CHANGES
# For noarch packages: sitelib
%{python3_sitelib}/*


%changelog
* Fri Jun 17 2011 Adam Huffman <bloch@verdurin.com> - 1.0.1-1
- initial version

