%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Morse
Summary:	Convert-Recode perl module
Summary(pl):	Modu³ perla Convert-Morse
Name:		perl-Convert-Morse
Version:	0.03
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-Morse - package to convert between ASCII and MORSE code.

%description -l pl
Convert-Morse - pakiet do konwersji miêdzy ASCII i kodem MORSE'a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Convert/Morse.pm
%{_mandir}/man3/*
