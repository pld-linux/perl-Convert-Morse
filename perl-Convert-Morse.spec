%include	/usr/lib/rpm/macros.perl
Summary:	Convert-Recode perl module
Summary(pl):	Modu³ perla Convert-Morse
Name:		perl-Convert-Morse
Version:	0.0.2
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-Morse-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-Morse - package to convert between ASCII and MORSE code.

%description -l pl
Convert-Morse - pakiet do konwersji miêdzy ASCII i kodem MORSE'a.

%prep
%setup -q -c -n Convert-Morse-%{version}
%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Convert/Morse
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz
%{perl_sitelib}/Convert/Morse.pm
%{perl_sitearch}/auto/Convert/Morse
%{_mandir}/man3/*
