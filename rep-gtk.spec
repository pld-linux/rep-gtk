Summary:	GTK+ binding for librep Lisp environment
Name:		rep-gtk
Version:	0.14
Release:	1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://rep-gtk.sourceforge.net/pub/rep-gtk/%{name}-%{version}.tar.gz
Patch0:		rep-gdkcolor.patch
URL:		http://rep-gtk.sourceforge.net/
BuildRequires:	librep-devel >= 0.13
BuildRequires:	librep-jl >= 0.13
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libglade-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a binding of GTK+ for the librep Lisp interpreter. It is based
on Marius Vollmer's guile-gtk package (initially version 0.15, updated
to 0.17), with a new glue-code generator.

%package libglade
Summary:	librep binding for the libglade library for loading user interfaces
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description libglade
This is a binding of libglade for the librep Lisp interpreter.
libglade allows applications to dynamically load XML descriptions of
GTK+ widget hierarchies. These hierarchies may be created by the GLADE
GUI builder.

%package gnome
Summary:	GNOME binding for librep
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description gnome
This is a binding of the various GNOME libraries for the librep Lisp
interpreter. It include support for the basic GNOME functions, the
GNOME user interface widgets, and the GNOME Canvas architecture.

%prep
%setup -q
%patch0 -p1

%build
autoconf
%configure \
	--without-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libexecdir}/rep/%{_host}/lib*.so*

gzip -9nf README README.guile-gtk ChangeLog *.defs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz README.guile-gtk.gz ChangeLog.gz gtk-1.2.defs.gz
%doc gdk-1.2.defs.gz
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/sgtk-types.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/sgtk-types.la
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/gtk.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/gtk.la

%files libglade
%defattr(644,root,root,755)
%doc libglade.defs.gz examples/test-libglade examples/simple.glade
%doc examples/rep-ui examples/rep-ui.glade
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/libglade.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/libglade.la

%files gnome
%defattr(644,root,root,755)
%doc examples/gnome-test examples/canvas-test
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/gnome*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/gnome*.la
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/libglade-gnome.so*
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/libglade-gnome.la
