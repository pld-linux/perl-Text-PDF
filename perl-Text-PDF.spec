%include	/usr/lib/rpm/macros.perl
Summary:	Text-PDF perl module
Summary(pl):	Modu³ perla Text-PDF
Name:		perl-Text-PDF
Version:	0.12
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-PDF-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Font-TTF
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-PDF - PDF manipulation module.

%description -l pl
Text-PDF umo¿liwia operowanie na plikach PDF.

%prep
%setup -q -n Text-PDF-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/PDF
%{_mandir}/man3/*
