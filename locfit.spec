Name:           locfit
Version:        1,5-6
Release:        1%{?dist}
Summary:        Local regression, likelihood and density estimation

Group:		Applications/Engineering
License:        GPLv2+
URL:		http://cm.bell-labs.com/cm/ms/departments/sia/project/locfit/index.html
Source0:        http://cm.bell-labs.com/cm/ms/departments/sia/project/locfit/dist/locfit.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  
Requires:       

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc



%changelog
