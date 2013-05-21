%define upstream_name	 RPC-XML
%define upstream_version 0.74

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release:	6

Summary:	A set of classes for core data, message and XML handling
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/RPC/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Net::Server)
BuildRequires:  perl(LWP::UserAgent)
BuildArch:	noarch

%description
The RPC::XML package is a reference implementation of the XML-RPC
standard. As a reference implementation, it is geared more towards clarity and
readability than efficiency.

The package provides a set of classes for creating values to pass to the
constructors for requests and responses. These are lightweight objects, most
of which are implemented as tied scalars so as to associate specific type
information with the value. Classes are also provided for requests, responses,
faults (errors) and a parser based on the XML::Parser package from CPAN.

This module does not actually provide any transport implementation or
server basis. For these, see RPC::XML::Client and RPC::XML::Server,
respectively.

%package	Apache
Summary:	RPC server as an Apache/mod_perl content handler
Group:		Development/Perl

%description	Apache
RPC server as an Apache/mod_perl content handler.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

# make tests don't work
# make test

%install
%makeinstall_std

%files
%doc ChangeLog README*
%{_bindir}/*
%{perl_vendorlib}/RPC
%{perl_vendorlib}/auto/RPC
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Apache*
%{_mandir}/man1/*

%files Apache
%doc README.apache2
%{perl_vendorlib}/Apache
%{_mandir}/man3/Apache*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.740.0-4mdv2012.0
+ Revision: 765636
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.740.0-2
+ Revision: 667299
- mass rebuild

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.740.0-1
+ Revision: 636158
- new version

* Wed Mar 17 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.730.0-1mdv2011.0
+ Revision: 523436
- update to 0.73

* Mon Dec 14 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.720.0-1mdv2010.1
+ Revision: 478548
- update to 0.72

* Tue Dec 08 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.710.0-1mdv2010.1
+ Revision: 474745
- update to 0.71

* Fri Sep 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.690.0-1mdv2010.0
+ Revision: 430459
- update to 0.69

* Fri Jul 10 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.670.0-1mdv2010.0
+ Revision: 394272
- update to 0.67
- using %%perl_convert_version
- fixed license field

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.66-1mdv2010.0
+ Revision: 394089
- update to new version 0.66

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.65-1mdv2010.0
+ Revision: 387018
- update to new version 0.65

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.64-1mdv2009.1
+ Revision: 292342
- update to new version 0.64

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.60-2mdv2009.0
+ Revision: 265434
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.60-1mdv2009.0
+ Revision: 193925
- update to new version 0.60

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.59-3mdv2008.1
+ Revision: 180543
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.59-2mdv2008.0
+ Revision: 86832
- rebuild


* Sat Jul 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.59-1mdv2007.0
- New version 0.59
- spec cleanup
- fix directory ownership

* Tue Oct 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.58-2mdk
- Fix BuildRequires

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.58-1mdk
- initial Mandriva package

