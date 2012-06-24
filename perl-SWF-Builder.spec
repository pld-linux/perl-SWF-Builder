#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SWF
%define	pnam	Builder
Summary:	SWF::Builder - create SWF movie
Summary(pl):	SWF::Builder - tworzenie film�w SWF
Name:		perl-SWF-Builder
Version:	0.07
Release:	0.2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/Y/YS/YSAS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d0857d07b52df777626019c9775ea27
URL:		http://search.cpan.org/dist/SWF-Builder/
%if %{with tests}
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Font-TTF >= 0.34
BuildRequires:	perl-SWF-File >= 0.29
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Font-TTF >= 0.34
Requires:	perl-SWF-File >= 0.29
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWF::Builder is a wrapper of SWF::File. It provides an easy way to
create SWF6 movie.

%description -l pl
SWF::Builder to wrapper na SWF::File. Dostarcza prosty spos�b na
tworzenie film�w SWF6.

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
%doc Changes README
%attr(755,root,root) %{_bindir}/asc.plx
%{perl_vendorlib}/SWF/Builder.pm
%{perl_vendorlib}/SWF/Builder
%{_mandir}/man1/asc.plx.1*
%{_mandir}/man3/SWF::Builder*
