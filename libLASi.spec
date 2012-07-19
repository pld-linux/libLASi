Summary:	Unicode PostScript C++ stream output intetface library
Summary(pl.UTF-8):	Biblioteka wyjścia strumieniowego C++ do PostScriptu z Unikodem
Name:		libLASi
Version:	1.1.1
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/lasi/%{name}-%{version}.tar.gz
# Source0-md5:	bc5161b1d820db3dbcea24ce1c2ed5ec
URL:		http://lasi.sourceforge.net/
BuildRequires:	cmake >= 2.6.4
BuildRequires:	freetype-devel >= 2.2
BuildRequires:	libstdc++-devel
BuildRequires:	pango-devel
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	freetype >= 2.2
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
Requires:	freetype-devel >= 2.2
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
# cmake suite doesn't accept "PLD" build type, use "Release"
%cmake .. \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_CXX_FLAGS_RELEASE="%{rpmcxxflags} -DNDEBUG" \
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
%doc AUTHORS CONCATENATED_README.release ChangeLog NEWS README README.release
%attr(755,root,root) %{_libdir}/libLASi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libLASi.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/developer doc/user
%attr(755,root,root) %{_libdir}/libLASi.so
%{_includedir}/LASi.h
%{_pkgconfigdir}/lasi.pc
