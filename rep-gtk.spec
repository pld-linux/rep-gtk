Summary:	GTK+ binding for librep Lisp environment
Summary(es):	Conjuntos de componentes GTK para el ambiente LISP librep
Summary(ko):	librep Lisp 환경을 위한 GTK+ 바인딩
Summary(pl):	Interfejs GTK+ do 턳odowiska Lispa librep
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
nuevo generador de c�digo intermediario.

%description -l pl
To jest interfejs GTK+ do interpretera Lispa librep. Bazuje na
pakiecie guile-gtk Mariusa Vollmera (pocz켾kowo wersji 0.15, p撰niej
uaktualniono do 0.17) z nowym generatorem kodu.

%description -l pt_BR
Esse pacote cont�m um conjunto de componentes GTK para o interpretador
LISP librep. Ele � baseado no pacote guile-gtk, com um novo gerador de
c�digo intermedi�rio.

%package libglade
Summary:	librep binding for the libglade library for loading user interfaces
Summary(es):	librep binding for the libglade library for loading user interfaces
Summary(ko):	사용자 인터페이스를 읽어들이기 위한 libglade라이브러리의 librep 바인딩
Summary(pl):	Interfejs librep do biblioteki libglade
Summary(pt_BR):	V�nculos librep para a biblioteca libglade para carregamento de interfaces de usu�rio
Group:		Development/Languages
Requires:	%{name} = %{version}

%description libglade
This is a binding of libglade for the librep Lisp interpreter.
libglade allows applications to dynamically load XML descriptions of
GTK+ widget hierarchies. These hierarchies may be created by the GLADE
GUI builder.

%description libglade -l es
This is a binding of libglade for the librep Lisp interpreter.
libglade allows applications to dynamically load XML descriptions of
GTK+ widget hierarchies. These hierarchies may be created by the GLADE
GUI builder.

%description libglade -l pl
To jest interfejs libglade do interpretera Lispa librep. libglade
pozwala aplikacjom dynamicznie wczytywa� opisy XML hierarchii widget�w
GTK+.

%description libglade -l pt_BR
Este � um bind da libglade para o interpretador librep Lisp. A
libglade permite que as aplica寤es carreguem dinamicamente as
descri寤es XML das hierarquias de elementos gr�ficos (widgets) GTK+.
Essas hierarquias podem ser criadas com o GLADE GUI builder.

%package gnome
Summary:	GNOME binding for librep
Summary(es):	GNOME binding for librep
Summary(ko):	librep를 위한 GNOME바인딩
Summary(pl):	Interfejs GNOME do librep
Summary(pt_BR):	GNOME binding for librep
Group:		Development/Languages
Requires:	%{name} = %{version}

%description gnome
This is a binding of the various GNOME libraries for the librep Lisp
interpreter. It include support for the basic GNOME functions, the
GNOME user interface widgets, and the GNOME Canvas architecture.

%description gnome -l es
This is a binding of the various GNOME libraries for the librep Lisp
interpreter. It include support for the basic GNOME functions, the
GNOME user interface widgets, the GNOME Canvas architecture, and the
GNOME version of libglade.

%description gnome -l pl
To jest interfejs r璨nych bibliotek GNOME do interpretera Lispa
librep. Zawiera wsparcie dla podstawowych funkcji GNOME, widget�w
interfejsu u퓓tkownika GNOME, architektury GNOME Canvas.

%description gnome -l pt_BR
Este � um bind das v�rias bibliotecas GNOME para o interpretador
librep Lisp. Inclui suporte �s fun寤es b�sicas do GNOME, os elementos
gr�ficos (widgets) da interface de usu�rio GNOME, a arquitetura GNOME
Canvas, e a vers�o GNOME da libglade.

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
