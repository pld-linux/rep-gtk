Summary:	GTK+ binding for librep Lisp environment
Summary(es):	Conjuntos de componentes GTK para el ambiente LISP librep
Summary(pl):	Interfejs GTK+ do ¶rodowiska Lispa librep
Summary(pt_BR):	Conjuntos de componentes GTK para o ambiente LISP librep
Name:		rep-gtk
Version:	0.15
Release:	8
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	ftp://rep-gtk.sourceforge.net/pub/rep-gtk/%{name}-%{version}.tar.gz
Patch0:		rep-gdkcolor.patch
URL:		http://rep-gtk.sourceforge.net/
BuildRequires:	librep-devel >= 0.13
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libglade-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	autoconf
BuildRequires:	automake
%define		repexecdir	%(rep-config --execdir)
Requires:	%{repexecdir}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}

%description
This is a binding of GTK+ for the librep Lisp interpreter. It is based
on Marius Vollmer's guile-gtk package (initially version 0.15, updated
to 0.17), with a new glue-code generator.

%description -l es
Este paquete contiene un conjunto de componentes GTK para el
interpretador LISP librep. Se basa en el paquete guile-gtk, con un
nuevo generador de código intermediario.

%description -l pl
To jest interfejs GTK+ do interpretera Lispa librep. Bazuje na
pakiecie guile-gtk Mariusa Vollmera (pocz±tkowo wersji 0.15, pó¼niej
uaktualniono do 0.17) z nowym generatorem kodu.

%description -l pt_BR
Esse pacote contém um conjunto de componentes GTK para o interpretador
LISP librep. Ele é baseado no pacote guile-gtk, com um novo gerador de
código intermediário.

%package libglade
Summary:	librep binding for the libglade library for loading user interfaces
Summary(es):	librep binding for the libglade library for loading user interfaces
Summary(pl):	Interfejs librep do biblioteki libglade
Summary(pt_BR):	Vínculos librep para a biblioteca libglade para carregamento de interfaces de usuário
Group:		Development/Languages
Requires:	%{name} = %{version}

%description libglade
This is a binding of libglade for the librep Lisp interpreter.
libglade allows applications to dynamically load XML descriptions of
GTK+ widget hierarchies. These hierarchies may be created by the GLADE
GUI builder.

%description -l es libglade
This is a binding of libglade for the librep Lisp interpreter.
libglade allows applications to dynamically load XML descriptions of
GTK+ widget hierarchies. These hierarchies may be created by the GLADE
GUI builder.

%description libglade -l pl
To jest interfejs libglade do interpretera Lispa librep. libglade
pozwala aplikacjom dynamicznie wczytywaæ opisy XML hierarchii widgetów
GTK+.

%description -l pt_BR libglade
Este é um bind da libglade para o interpretador librep Lisp. A
libglade permite que as aplicações carreguem dinamicamente as
descrições XML das hierarquias de elementos gráficos (widgets) GTK+.
Essas hierarquias podem ser criadas com o GLADE GUI builder.

%package gnome
Summary:	GNOME binding for librep
Summary(es):	GNOME binding for librep
Summary(pl):	Interfejs GNOME do librep
Summary(pt_BR):	GNOME binding for librep
Group:		Development/Languages
Requires:	%{name} = %{version}

%description gnome
This is a binding of the various GNOME libraries for the librep Lisp
interpreter. It include support for the basic GNOME functions, the
GNOME user interface widgets, and the GNOME Canvas architecture.

%description -l es gnome
This is a binding of the various GNOME libraries for the librep Lisp
interpreter. It include support for the basic GNOME functions, the
GNOME user interface widgets, the GNOME Canvas architecture, and the
GNOME version of libglade.

%description gnome -l pl
To jest interfejs ró¿nych bibliotek GNOME do interpretera Lispa
librep. Zawiera wsparcie dla podstawowych funkcji GNOME, widgetów
interfejsu u¿ytkownika GNOME, architektury GNOME Canvas.

%description -l pt_BR gnome
Este é um bind das várias bibliotecas GNOME para o interpretador
librep Lisp. Inclui suporte às funções básicas do GNOME, os elementos
gráficos (widgets) da interface de usuário GNOME, a arquitetura GNOME
Canvas, e a versão GNOME da libglade.

%prep
%setup -q
%patch0 -p1

%build
autoconf
cp -f /usr/share/automake/config.* .
%configure \
	--without-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README README.guile-gtk ChangeLog *.defs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz README.guile-gtk.gz ChangeLog.gz *.defs.gz

%dir %{repexecdir}/gui

%attr(755,root,root) %{repexecdir}/sgtk-types.so
%attr(755,root,root) %{repexecdir}/sgtk-types.la
%attr(755,root,root) %{repexecdir}/gtk.so
%attr(755,root,root) %{repexecdir}/gtk.la
%attr(755,root,root) %{repexecdir}/gdk-pixbuf.so
%attr(755,root,root) %{repexecdir}/gdk-pixbuf.la

%dir %{repexecdir}/gui/gtk

%attr(755,root,root) %{repexecdir}/gui/gtk.so
%attr(755,root,root) %{repexecdir}/gui/gtk.la

%attr(755,root,root) %{repexecdir}/gui/gtk/gdk-pixbuf.la
%attr(755,root,root) %{repexecdir}/gui/gtk/gdk-pixbuf.so
%attr(755,root,root) %{repexecdir}/gui/gtk/gtk.la
%attr(755,root,root) %{repexecdir}/gui/gtk/gtk.so
%attr(755,root,root) %{repexecdir}/gui/gtk/types.la
%attr(755,root,root) %{repexecdir}/gui/gtk/types.so

%files libglade
%defattr(644,root,root,755)
%doc libglade.defs.gz examples/test-libglade examples/simple.glade
%doc examples/rep-ui examples/rep-ui.glade
%attr(755,root,root) %{repexecdir}/libglade.so
%attr(755,root,root) %{repexecdir}/libglade.la
%attr(755,root,root) %{repexecdir}/gui/gtk/libglade.la
%attr(755,root,root) %{repexecdir}/gui/gtk/libglade.so

%files gnome
%defattr(644,root,root,755)
%doc examples/gnome-test examples/canvas-test

%attr(755,root,root) %{repexecdir}/gnome*.so
%attr(755,root,root) %{repexecdir}/gnome*.la
%attr(755,root,root) %{repexecdir}/libglade-gnome.so*
%attr(755,root,root) %{repexecdir}/libglade-gnome.la

%dir %{repexecdir}/gui/gnome

%attr(755,root,root) %{repexecdir}/gui/gnome.so
%attr(755,root,root) %{repexecdir}/gui/gnome.la
%attr(755,root,root) %{repexecdir}/gui/gnome/canvas-pixbuf.la
%attr(755,root,root) %{repexecdir}/gui/gnome/canvas-pixbuf.so
%attr(755,root,root) %{repexecdir}/gui/gnome/canvas.la
%attr(755,root,root) %{repexecdir}/gui/gnome/canvas.so
%attr(755,root,root) %{repexecdir}/gui/gnome/lib.la
%attr(755,root,root) %{repexecdir}/gui/gnome/lib.so
%attr(755,root,root) %{repexecdir}/gui/gnome/libglade.la
%attr(755,root,root) %{repexecdir}/gui/gnome/libglade.so
%attr(755,root,root) %{repexecdir}/gui/gnome/ui.la
%attr(755,root,root) %{repexecdir}/gui/gnome/ui.so
