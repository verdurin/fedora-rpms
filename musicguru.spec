Name:           dupeGuru-ME
Version: 	1.4.3
Release:        1%{?dist}
Summary:        Find duplicate songs

Group:          Applications/Multimedia
License:        Freely redistributable
URL:            http://www.hardcoded.net/dupeguru_me/
Source0:        http://download.hardcoded.net/dupeguru-me_6.0.1_amd64.deb
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python3-devel
Requires:       

%description

dupeGuru Music Edition (ME for short) is a tool to find duplicate
songs in your music collection. It can scan filenames, tags or
contents. dupeGuru ME is a big brother of dupeGuru. It does everything
dupeGuru does, but it has more information columns (such as bitrate,
duration, tags, etc..) and more scan types (filename with fields, tags
and audio content).



%prep
%setup -q -n hsoft-musicguru-632692b1211f


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
