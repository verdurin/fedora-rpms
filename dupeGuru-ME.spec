# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           dupeGuru-ME
Version:        
Release:        1%{?dist}
Summary:        

Group:          Development/Languages
License:        
URL:            
Source0:        
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      
BuildRequires:  python3-devel

%description


%prep
%setup -q


%build
%{__python3} configure.py
%{__python3} build.py
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="%{optflags}" %{__python3} setup.py build


%install
rm -rf %{buildroot}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE README
# For noarch packages: sitelib
%{python3_sitelib}/*
# For arch-specific packages: sitearch
%{python3_sitearch}/*


%changelog
