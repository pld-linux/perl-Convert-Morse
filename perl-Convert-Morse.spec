#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	Morse
Summary:	Convert-Recode - convert between ASCII text and MORSE alphabet
Summary(pl.UTF-8):	Convert::Morse - konwersja pomiędzy tekstem ASCII i alfabetem MORSE'a
Name:		perl-Convert-Morse
Version:	0.05
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Convert/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	785cf77e1057e19f8a6e735a4736a4b1
URL:		http://search.cpan.org/dist/Config-Morse/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::Morse Perl module lets you convert between normal ASCII text
and international MORSE code.  You can redefine the token sets, if you
like.

%description -l pl.UTF-8
Moduł Perla Convert::Morse pozwala na konwersję pomiędzy zwykłym
tekstem w ASCII a muiędzynarodowym kodem MORSE'a. Umożliwia
zredefiniowanie znaczenia kodów MORSE'a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
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
%doc CHANGES README
%{perl_vendorlib}/Convert/Morse.pm
%{_mandir}/man3/*
