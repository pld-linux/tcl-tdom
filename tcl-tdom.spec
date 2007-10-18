Summary:	XML parsing for Tcl
Summary(pl.UTF-8):	Analizowanie XML-a dla Tcl-a
Name:		tcl-tdom
Version:	0.8.2
Release:	1
License:	MPL 1.1
Group:		Development/Languages/Tcl
Source0:	http://www.tdom.org/files/tDOM-%{version}.tgz
# Source0-md5:	67790846eb5ec13852a3bf3c382d86dc
URL:		http://tclxml.sourceforge.net/tclxml.html
BuildRequires:	tcl-devel >= 8.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tDOM combines high performance XML data processing with easy and
powerful Tcl scripting functionality. tDOM should be one of the
fastest ways to manipulate XML with a scripting language and uses very
little memory in the process (for example the DOM tree of the XML
recommendation in XML (160K) needs only about 450K in memory)!
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
%{_includedir}/*.h
%dir %{_libdir}/tdom*.*
%attr(755,root,root) %{_libdir}/tdom*.*/*.so
%{_libdir}/tdom*.*/*.a
%{_libdir}/tdom*.*/*.tcl
%dir %{_libdir}/*.sh
%{_mandir}/mann/*
