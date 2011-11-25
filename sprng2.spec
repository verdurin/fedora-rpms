Name:           sprng2
Version:        2.0
Release:        1%{?dist}
Summary:        Scalable Parallel Pseudo Random Number Generators

Group:		Applications/Engineering
License:        NCBI
URL:            http://sprng.cs.fsu.edu/Version2.0/index.html
Source0:        http://sprng.cs.fsu.edu/Version2.0/sprng2.0b.tar.gz
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
