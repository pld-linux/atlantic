Summary:	Setup and diagnostic program for ISA NE2000 Ethernet adapters
Summary(pl.UTF-8):	Program konfiguracyjny i diagnostyczny do kart sieciowych ISA NE2000
Name:		atlantic
# note: version taken from CVS rev.
Version:	1.7
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.scyld.com/pub/diag/atlantic.c
# Source0-md5:	56e307f86a7d3a428d599b6ad1598609
URL:		http://www.scyld.com/diag/atlantic.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debugcflags	-O1 -g

%description
This is a setup and diagnostic program for ISA NE2000 Ethernet
adapters. It has specific support for configuring the National
Semiconductor AT/LANTIC DP83905 used in on ISA Ethernet adapters such
as the NE2000plus. It also works several work-alike chips from other
vendors.

%description -l pl.UTF-8
Ten pakiet zawiera program konfiguracyjny i diagnostyczny do kart
sieciowych ISA NE2000. Został napisany dla kart na układzie National
Semiconductor AT/LANTIC DP83905, użytym do kart sieciowych ISA takich
jak NE2000plus. Działa też z niektórymi podobnie zachowującymi się
układami innych producentów.

%prep
%setup -q -c -T

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o atlantic %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install atlantic $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
