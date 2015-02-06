%define upstream_name   Authen-Simple-LDAP
%define upstream_version 0.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.3
Release:	3

Summary:	Simple LDAP authentication
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Authen/Authen-Simple-LDAP-0.3.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Authen::Simple)
BuildRequires:	perl(Net::LDAP)
BuildRequires:	perl(Module::Build::Compat)

BuildArch:	noarch

%description
Authenticate against a LDAP service.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.200.0-4mdv2011.0
+ Revision: 654189
- rebuild
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 504580
- rebuild using %%perl_convert_version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2-1mdv2009.1
+ Revision: 292550
- import perl-Authen-Simple-LDAP


* Thu Oct 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2-1mdv2009.1
- initial mdv release, generated with cpan2dist

