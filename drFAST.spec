Name:           drFAST
Version:        0.0.0.3
Release:        1%{?dist}
Summary:        di-base read Fast Alignment Search Tool

Group:          Applications/Engineering
License:        Redistributable
URL:            http://drfast.sourceforge.net
Source0:        http://downloads.sourceforge.net/drfast/%{name}-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  zlib-devel


%description

drFAST is designed to map short reads generated with the AB Solid platform to 
reference genome assemblies; in a fast and memory-efficient manner.

%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="%{optflags} -c" LDFLAGS="-lz -lm"


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 drfast %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.txt
%{_bindir}/drfast



%changelog
* Fri Jul 29 2011 Adam Huffman <bloch@verdurin.com> - 0.0.0.3-1
- initial version

