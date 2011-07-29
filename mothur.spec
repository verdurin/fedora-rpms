Name:           mothur
Version:        1.20.3
Release:        1%{?dist}
Summary:	Computational microbial ecology tool 

Group:		Appllications/Engineering
License:	GPLv3
URL:		http://www.mothur.org
Source0:	http://www.mothur.org/w/images/4/42/Mothur.1.20.3.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	ncurses-devel
BuildRequires:	readline-devel


%description

The mothur project was initiated by Dr. Patrick Schloss and his
software development team in the Department of Microbiology &
Immunology at The University of Michigan. This project seeks to
develop a single piece of open-source, expandable software to fill the
bioinformatics needs of the microbial ecology community. The authors
have incorporated the functionality of dotur, sons, treeclimber,
s-libshuff, unifrac, and much more. In addition to improving the
flexibility of these algorithms, they have added a number of other
features including calculators and visualization tools.

%prep
%setup -q -n Mothur.source

#Remove OS X files
rm -rf __MACOSX*

%build


make %{?_smp_mflags} CXXFLAGS="%{optflags} -DUSE_READLINE -DUSE_COMPRESSION \
-DRELEASE_DATE="\"7/13/2011\"" -DVERSION="\"1.20.3\"""


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc



%changelog
* Tue Jul 19 2011 Adam Huffman <bloch@verdurin.com> - 1.20.3-1
- initial version

