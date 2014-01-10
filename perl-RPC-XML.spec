%define modname	RPC-XML
%define modver 0.77

Summary:	A set of classes for core data, message and XML handling
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:	http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/RPC/RPC-XML-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Net::Server)
BuildRequires:	perl(LWP::UserAgent)

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# make tests don't work
#make test

%install
%makeinstall_std

%files
%doc ChangeLog README*
%{_bindir}/*
# %{perl_vendorlib}/RPC
# %{perl_vendorlib}/auto/RPC
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Apache*
%{_mandir}/man1/*
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML.pm
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/Client.pm
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/Parser.pm
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/Parser/XMLLibXML.pm
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/Parser/XMLParser.pm
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/ParserFactory.pm
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/Procedure.pm
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/Server.pm
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/identity.xpl
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/introspection.xpl
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/listMethods.xpl
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/methodHelp.xpl
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/methodSignature.xpl
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/multicall.xpl
%{_libdir}/perl5/vendor_perl/5.16.3/RPC/XML/status.xpl

%files Apache
%doc README.apache2
%{perl_vendorlib}/Apache
%{_mandir}/man3/Apache*


