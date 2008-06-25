# TODO: system expat
Summary:	XML parsing for Tcl
Summary(pl.UTF-8):	Analizator XML-a dla Tcl-a
Name:		tcl-tdom
Version:	0.8.2
Release:	1
License:	MPL 1.1
Group:		Development/Languages/Tcl
Source0:	http://www.tdom.org/files/tDOM-%{version}.tgz
# Source0-md5:	67790846eb5ec13852a3bf3c382d86dc
URL:		http://www.tdom.org/
BuildRequires:	tcl-devel >= 8.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tDOM combines high performance XML data processing with easy and
powerful Tcl scripting functionality. tDOM should be one of the
fastest ways to manipulate XML with a scripting language and uses very
little memory in the process (for example the DOM tree of the XML
recommendation in XML (160K) needs only about 450K in memory)!

%description -l pl.UTF-8
tDOM łączy wysoko wydajne przetwarzanie danych XML z łatwą i
dającą duże możliwości funkcjonalnością skryptową Tcl-a. tDOM powinien
być jednym z najszybszych sposobów obróbki XML-a z poziomu języków
skryptowych; używa bardzo mało pamięci (np. drzewo DOM rekomendacji
XML w XML-u, mające 160kB, potrzebuje tylko 450kB pamięci).

%package devel
Summary:	C development files for tDOM module
Summary(pl.UTF-8):	Pliki programistyczne C dla modułu tDOM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	tcl-devel >= 8.4.3
# for header, even if system expat is not used
Requires:	expat-devel

%description devel
C development files for tDOM module.

%description devel -l pl.UTF-8
Pliki programistyczne C dla modułu tDOM.

%prep
%setup -q -n tDOM-%{version}

%build
%configure \
%if "%{_lib}" == "lib64"
	--enable-64bit \
%endif
	--enable-threads
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README doc/*.html
%dir %{_libdir}/tdom%{version}
%attr(755,root,root) %{_libdir}/tdom%{version}/libtdom%{version}.so
%{_libdir}/tdom%{version}/tdom.tcl
%{_libdir}/tdom%{version}/pkgIndex.tcl
%{_mandir}/mann/dom*.n*
%{_mandir}/mann/expat*.n*
%{_mandir}/mann/tdomcmd.n*
%{_mandir}/mann/tnc.n*

%files devel
%defattr(644,root,root,755)
%{_libdir}/tdom%{version}/libtdomstub%{version}.a
%attr(755,root,root) %{_libdir}/tdomConfig.sh
%{_includedir}/tdom.h
