%define	module	Net-Kismet
%define name	perl-%{module}
%define version	0.04
%define release	4mdk

Summary:	Net::Kismet perl module
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Requires:	perl
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.kismetwireless.net/
Source:		%{module}-%{version}.tar.bz2
BuildArch:	noarch

%description
A perl module to make writing Kismet clients in perl much simpler.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README MANIFEST Changes
%{perl_vendorlib}/Net/*
%_mandir/*/*

