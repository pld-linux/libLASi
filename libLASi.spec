Summary:	Unicode PostScript C++ stream output intetface library
Summary(pl.UTF-8):	Biblioteka wyjścia strumieniowego C++ do PostScriptu z Unikodem
Name:		libLASi
Version:	1.1.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/lasi/%{name}-%{version}.tar.gz
# Source0-md5:	f18091569ed4fface75453b097c67459
URL:		http://lasi.sourceforge.net/
BuildRequires:	cmake >= 2.4.5
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pango-devel
BuildRequires:	rpmbuild(macros) >= 1.471
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libLASi is library that provides a C++ stream output interface (with
operator <<) for creating PostScript documents that can contain
characters from any of the script and symbol blocks supported in
Unicode and by the Pango layout engine.

%description -l pl.UTF-8
libLASi to biblioteka udostępniająca interfejs wyjścia strumieniowego
C++ (przy użyciu operatora <<) do tworzenia dokumentów w PostScripcie
zawierających znaki z dowolnego alfabetu oraz bloki symboli
obsługiwane przez Unikod i silnik Pango.

%package devel
Summary:	Header files for libLASi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libLASi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel
Requires:	libstdc++-devel
Requires:	pango-devel

%description devel
Header files for libLASi library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libLASi.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DUSE_RPATH=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libLASi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libLASi.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/developer doc/user
%attr(755,root,root) %{_libdir}/libLASi.so
%{_includedir}/LASi.h
%{_pkgconfigdir}/lasi.pc
