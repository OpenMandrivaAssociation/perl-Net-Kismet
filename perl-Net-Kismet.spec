%define	module	Net-Kismet
%define name	perl-%{module}
%define version	0.04
%define release	10

Summary:	Net::Kismet perl module
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Requires:	perl
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		https://www.kismetwireless.net/
Source:		%{module}-%{version}.tar.bz2
BuildArch:	noarch

%description
A perl module to make writing Kismet clients in perl much simpler.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.04-8mdv2010.0
+ Revision: 430513
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.04-7mdv2009.0
+ Revision: 268624
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-6mdv2009.0
+ Revision: 210960
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.04-5mdv2008.0
+ Revision: 25252
- rebuild


* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.04-4mdk
- rebuild

* Mon Aug 18 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.04-3mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- don't use PREFIX
- use %%makeinstall_std macro

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-2mdk
- rebuild for new auto{prov,req}

* Mon Mar 17 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.04-1mdk
- new

