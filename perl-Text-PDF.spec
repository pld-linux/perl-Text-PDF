%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	PDF
Summary:	Text::PDF perl module
Summary(pl):	Modu³ perla Text::PDF
Name:		perl-Text-PDF
Version:	0.20
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-fix.patch
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Font-TTF
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::PDF - PDF manipulation module.

%description -l pl
Text::PDF umo¿liwia operowanie na plikach PDF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *txt
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Text/PDF
%{_mandir}/man3/*
