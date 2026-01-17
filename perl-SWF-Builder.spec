#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define	pdir	SWF
%define	pnam	Builder
Summary:	SWF::Builder - create SWF movie
Summary(pl.UTF-8):	SWF::Builder - tworzenie filmów SWF
Name:		perl-SWF-Builder
Version:	0.16
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/Y/YS/YSAS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1e879b1b70a6d23bed64e0c960918944
URL:		http://search.cpan.org/dist/SWF-Builder/
%if %{with tests}
BuildRequires:	perl-IO-Compress
BuildRequires:	perl-Font-TTF >= 0.34
BuildRequires:	perl-SWF-File >= 0.29
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Font-TTF >= 0.34
Requires:	perl-SWF-File >= 0.29
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(SWF::Builder::ExElement::Color::AddColor)

%description
SWF::Builder is a wrapper of SWF::File. It provides an easy way to
create SWF6 movie.

%description -l pl.UTF-8
SWF::Builder to wrapper na SWF::File. Dostarcza prosty sposób na
tworzenie filmów SWF6.

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
