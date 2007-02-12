#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	PDF
Summary:	Text::PDF perl module
Summary(pl.UTF-8):   Moduł perla Text::PDF
Name:		perl-Text-PDF
%define		base_version	0.29
Version:	%{base_version}a
Release:	1
# one module mentions License=Artistic
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2fdf4c3170e53a083715888237914a9b
Patch0:		%{name}-fix.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Font-TTF
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::PDF - PDF manipulation module.

%description -l pl.UTF-8
Text::PDF umożliwia operowanie na plikach PDF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{base_version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *txt lib/Text/PDF/changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Text/PDF.pm
%dir %{perl_vendorlib}/Text/PDF
%{perl_vendorlib}/Text/PDF/*.pm
%{_mandir}/man3/*
