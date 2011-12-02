Name:           gnome-boxes
Version:	3.3.2
Release:        1%{?dist}
Summary:        Simple access to remote or virtual systeems

Group:          System/Virtualizationq
License:        LGPLv2
URL:            http://live.gnome.org/Boxes
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gnome-boxes/3.3/gnome-boxes-3.3.2.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libosinfo-devel
BuildRequires:	gtk3-devel
BuildRequires:	qemu-devel
BuildRequires:	gudev-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	libvirt-devel


%description
A simplified, user-friendly application for remote connections and for
easy to use local virtualization.

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
* Fri Dec  2 2011 Adam Huffman <verdurin@fedoraproject.org> - 3.3.2-1
- initial version

