#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	PDF
Summary:	Text::PDF perl module
Summary(pl):	Modu³ perla Text::PDF
Name:		perl-Text-PDF
Version:	0.23
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-fix.patch
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Font-TTF
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *txt lib/Text/PDF/changes
%attr(755,root,root) %{_bindir}/*
%dir %{perl_sitelib}/Text/PDF
%{perl_sitelib}/Text/PDF/*.pm
%{_mandir}/man3/*
