Name:           ultrascan3
Version:        1
Release:        1%{?dist}
Summary:        Ultrascan

Group:          Applications/Engineering
License:        GPLv3
URL:		http://www.ultrascan.uthscsa.edu/
Source0:        ultrascan3-src-r1130.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  qt-devel
BuildRequires:	qwt-devel
BuildRequires:	qca
BuildRequires:	qca-ossl
BuildRequires:	qtsingleapplication-devel
BuildRequires:	openssl-devel
BuildRequires:	mysql-devel
BuildRequires:	doxygen
BuildRequires:	qconf
BuildRequires:	qwtplot3d-qt4-devel
BuildRequires:	uuid-c++-devel

%description

UltraScan blah

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
