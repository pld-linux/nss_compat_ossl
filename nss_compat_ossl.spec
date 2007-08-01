Summary:	Source-level compatibility library for OpenSSL to NSS porting
Summary(pl.UTF-8):	Biblioteka kompatybilności do portowania z OpenSSL-a do NSS
Name:		nss_compat_ossl
Version:	0.9.1
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://directory.fedoraproject.org/sources/%{name}-%{version}.tar.gz
# Source0-md5:	765c1426fc61b5c67c17fca0a87405cb
Patch0:		%{name}-headers.patch
BuildRequires:	nspr-devel >= 4
BuildRequires:	nss-devel >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides a source-level compatibility layer to aid
porting programs that use OpenSSL to use the NSS instead.

%description -l pl.UTF-8
Ta biblioteka udostępnia warstwę kompatybilności na poziomie źródeł
pomagającą portować programy wykorzystujące bibliotekę OpenSSL do
używania zamiast niej biblioteki NSS

%package devel
Summary:	Header file for nss_compat_ossl library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki nss_compat_ossl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	nspr-devel >= 4
Requires:	nss-devel >= 3

%description devel
Header file for doing porting work from OpenSSL to NSS.

%description devel -l pl.UTF-8
Plik nagłówkowy do portowania z OpenSSL-a do NSS.

%package static
Summary:	Static nss_compat_ossl library
Summary(pl.UTF-8):	Statyczna biblioteka nss_compat_ossl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nss_compat_ossl library.

%description static -l pl.UTF-8
Statyczna biblioteka nss_compat_ossl.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libnss_compat_ossl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnss_compat_ossl.so
%{_libdir}/libnss_compat_ossl.la
%{_includedir}/nss_compat_ossl

%files static
%defattr(644,root,root,755)
%{_libdir}/libnss_compat_ossl.a
