Name:           drfast
Version:        0.0.0.3
Release:        1%{?dist}
Summary:        di-base read Fast Alignment Search Tool

Group:          Applications/Engineering
License:        Redistributable
URL:            http://drfast.sourceforge.net
Source0:        
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  


%description

drFAST is designed to map short reads generated with the AB Solid platform to 
reference genome assemblies; in a fast and memory-efficient manner.

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
