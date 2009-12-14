%define upstream_name	 RPC-XML
%define upstream_version 0.72

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	A set of classes for core data, message and XML handling
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/RPC/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Net::Server)
BuildRequires:  perl(LWP::UserAgent)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# make tests don't work
# make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README*
%{_bindir}/*
%{perl_vendorlib}/RPC
%{perl_vendorlib}/auto/RPC
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Apache*
%{_mandir}/man1/*

%files Apache
%defattr(-,root,root)
%doc README.apache2
%{perl_vendorlib}/Apache
%{_mandir}/man3/Apache*

