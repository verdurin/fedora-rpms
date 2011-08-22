Name:           mothur
Version:        1.21.1
Release:        2%{?dist}
Summary:	Computational microbial ecology tool 

Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.mothur.org
Source0:	http://www.mothur.org/w/images/4/42/Mothur.%{version}.zip
patch0:		%{name}-makefile.patch
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
#Deal with mistakenly included OS X files
#unzip %{SOURCE0} -x __MACOSX* .DS_Store
%setup -q   -n Mothur.source
rm -rf __MACOSX* .DS_Store
%patch0 -p1

%build


make  
#make %{?_smp_mflags} CXXFLAGS+="%{optflags}"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc



%changelog
* Fri Aug 19 2011 Adam Huffman <bloch@verdurin.com> - 1.21.1-2
- patch makefile to fix compilation flags

* Fri Aug 19 2011 Adam Huffman <bloch@verdurin.com> - 1.21.1-1
- update to upstream 1.21.1

* Fri Jul 29 2011 Adam Huffman <bloch@verdurin.com> - 1.21.0-1
- update to upstream release 1.21.0

* Tue Jul 19 2011 Adam Huffman <bloch@verdurin.com> - 1.20.3-1
- initial version

