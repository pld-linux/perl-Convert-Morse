%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Morse
Summary:	Convert-Recode - convert between ASCII text and MORSE alphabet
Summary(pl):	Convert::Morse - konwersja pomi�dzy tekstem ASCII i alfabetem MORSE'a
Name:		perl-Convert-Morse
Version:	0.03
Release:	6
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f6df3b07efba69a1fe4b87870c706dc7
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::Morse Perl module lets you convert between normal ASCII text
and international MORSE code.  You can redefine the token sets, if you
like.

%description -l pl
Modu� Perla Convert::Morse pozwala na konwersj� pomi�dzy zwyk�ym
tekstem w ASCII a mui�dzynarodowym kodem MORSE'a. Umo�liwia
zredefiniowanie znaczenia kod�w MORSE'a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Convert/Morse.pm
%{_mandir}/man3/*
