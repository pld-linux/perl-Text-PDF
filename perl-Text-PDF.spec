%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Text-PDF perl module
Summary(pl):	Modu³ perla Text-PDF
Name:		perl-Text-PDF
Version:	0.06
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-PDF-%{version}.tar.gz
Patch:		perl-Text-PDF-makefile.patch
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-Compress-Zlib
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-Compress-Zlib
Requires:	perl-Font-TTF
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Text-PDF - PDF manipulation module.

%description -l pl
Text-PDF umo¿liwia operowanie na plikach PDF.

%prep
%setup -q -n Text-PDF-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/PDF
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt.gz

%{perl_sitelib}/Text/PDF
%{perl_sitearch}/auto/Text/PDF

%{_mandir}/man3/*
