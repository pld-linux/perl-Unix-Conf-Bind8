#
# Conditional build:
%bcond_with	tests	# do perform "make test"
#
%define		pdir	Unix
%define		pnam	Conf-Bind8
Summary:	Unix::Conf::Bind8 - manipulating a Bind8 conf and associated zone record files
Summary(pl.UTF-8):	Unix::Conf::Bind8 - manipulowanie plikami konfiguracyjnymi Bind8 i plikami stref
Name:		perl-Unix-Conf-Bind8
Version:	0.3
Release:	3
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a31aae28a2deb512d8b49ce1eaca17db
Patch0:		%{name}-require_bareword.patch
URL:		http://www.extremix.net/UnixConf/
BuildRequires:	perl-Unix-Conf
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unix::Conf::Bind8 - Front end for a suite of classes for manipulating
a Bind8 conf and associated zone record files. Allows easy manipulation 
of files, zones, acls and other entries in Bind8 config file.

%description -l pl.UTF-8
Unix::Conf::Bind8 jest zestawem modułów pozwalających w łatwy sposób
czytać oraz modyfikować pliki konfiguracyjne Bind8 oraz pliki stref.
Pozwala w łatwy sposób dodawać następne strefy, typy logów oraz inne
wpisy mogące znajdować się w konfiguracji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
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
%doc Changes README
%{perl_vendorlib}/Unix/Conf/Bind8.pm
%dir %{perl_vendorlib}/Unix/Conf/Bind8
%{perl_vendorlib}/Unix/Conf/Bind8/*.pm
%dir %{perl_vendorlib}/Unix/Conf/Bind8/Conf
%{perl_vendorlib}/Unix/Conf/Bind8/Conf/*.pm
%dir %{perl_vendorlib}/Unix/Conf/Bind8/DB
%{perl_vendorlib}/Unix/Conf/Bind8/DB/*.pm
%dir %{perl_vendorlib}/Unix/Conf/Bind8/Conf/Logging
%{perl_vendorlib}/Unix/Conf/Bind8/Conf/Logging/Channel.pm
%{_mandir}/man3/*
