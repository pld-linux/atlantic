Summary:	Setup and diagnostic program for ISA NE2000 Ethernet adapters
Summary(pl):	Program konfiguracyjny i diagnostyczny do kart sieciowych ISA NE2000
Name:		atlantic
# note: version taken from CVS rev.
Version:	1.7
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.scyld.com/pub/diag/atlantic.c
URL:		http://www.scyld.com/diag/atlantic.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debugcflags	-O1 -g

%description
This is a setup and diagnostic program for ISA NE2000 Ethernet
adapters. It has specific support for configuring the National
Semiconductor AT/LANTIC DP83905 used in on ISA Ethernet adapters such
as the NE2000plus. It also works several work-alike chips from other
vendors.
				
%description -l pl
Ten pakiet zawiera program konfiguracyjny i diagnostyczny do kart
sieciowych ISA NE2000. Zosta³ napisany dla kart na uk³adzie National
Semiconductor AT/LANTIC DP83905, u¿ytym do kart sieciowych ISA takich
jak NE2000plus. Dzia³a te¿ z niektórymi podobnie zachowuj±cymi siê
uk³adami innych producentów.

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
