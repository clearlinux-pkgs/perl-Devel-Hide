#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-Hide
Version  : 0.0014
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-Hide-0.0014.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-Hide-0.0014.tar.gz
Summary  : 'Forces the unavailability of specified Perl modules (for testing)'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Devel-Hide-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Devel-Hide version 0.0010
=========================
Simple tool for developers which allows to hide
installed Perl modules. Used like this:

%package dev
Summary: dev components for the perl-Devel-Hide package.
Group: Development
Provides: perl-Devel-Hide-devel = %{version}-%{release}
Requires: perl-Devel-Hide = %{version}-%{release}

%description dev
dev components for the perl-Devel-Hide package.


%package perl
Summary: perl components for the perl-Devel-Hide package.
Group: Default
Requires: perl-Devel-Hide = %{version}-%{release}

%description perl
perl components for the perl-Devel-Hide package.


%prep
%setup -q -n Devel-Hide-0.0014
cd %{_builddir}/Devel-Hide-0.0014

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::Hide.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Devel/Hide.pm
