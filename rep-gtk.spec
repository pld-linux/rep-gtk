%define	dsnap	2002-06-11
%define snap    %(echo %{dsnap} | sed -e "s#-##g")
Summary:	GTK+ binding for librep Lisp environment
Summary(es):	Conjuntos de componentes GTK para el ambiente LISP librep
Summary(ko):	librep Lisp ȯ���� ���� GTK+ ���ε�
Summary(pl):	Interfejs GTK+ do �rodowiska Lispa librep
Summary(pt_BR):	Conjuntos de componentes GTK para o ambiente LISP librep
Name:		rep-gtk
Version:	0.17
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Languages
#Source0:	ftp://ftp.gnome.org/pub/gnome/sources/rep-gtk/0.16/%{name}-%{version}.tar.bz2
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0a7b4589f14ad89360863593f77232cf
Patch0:		rep-gdkcolor.patch
URL:		http://rep-gtk.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.3
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.1.1-3
BuildRequires:	libgnomecanvas-devel >= 2.0.1
BuildRequires:	librep-devel >= 0.16
BuildRequires:	pkgconfig
%define		repexecdir	%(rep-config --execdir)
Requires:	%{repexecdir}
Requires:	libgnomeui >= 2.1.1-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}

%description
This is a binding of GTK+ for the librep Lisp interpreter. It is based
on Marius Vollmer's guile-gtk package with a new glue-code generator.

%description -l es
Este paquete contiene un conjunto de componentes GTK para el
interpretador LISP librep. Se basa en el paquete guile-gtk, con un
nuevo generador de c�digo intermediario.

%description -l pl
To jest interfejs GTK+ do interpretera Lispa librep. Bazuje na
pakiecie guile-gtk Mariusa Vollmera z nowym generatorem kodu.

%description -l pt_BR
Esse pacote cont�m um conjunto de componentes GTK para o interpretador
LISP librep. Ele � baseado no pacote guile-gtk, com um novo gerador de
c�digo intermedi�rio.

%package libglade
Summary:	librep binding for the libglade library for loading user interfaces
Summary(es):	librep binding for the libglade library for loading user interfaces
Summary(ko):	����� �������̽��� �о���̱� ���� libglade���̺귯���� librep ���ε�
Summary(pl):	Interfejs librep do biblioteki libglade
Summary(pt_BR):	V�nculos librep para a biblioteca libglade para carregamento de interfaces de usu�rio
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}

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
libglade permite que as aplica��es carreguem dinamicamente as
descri��es XML das hierarquias de elementos gr�ficos (widgets) GTK+.
Essas hierarquias podem ser criadas com o GLADE GUI builder.

%package gnome
Summary:	GNOME binding for librep
Summary(es):	GNOME binding for librep
Summary(ko):	librep�� ���� GNOME���ε�
Summary(pl):	Interfejs GNOME do librep
Summary(pt_BR):	GNOME binding for librep
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}

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
To jest interfejs r�nych bibliotek GNOME do interpretera Lispa
librep. Zawiera wsparcie dla podstawowych funkcji GNOME, widget�w
interfejsu u�ytkownika GNOME, architektury GNOME Canvas.

%description gnome -l pt_BR
Este � um bind das v�rias bibliotecas GNOME para o interpretador
librep Lisp. Inclui suporte �s fun��es b�sicas do GNOME, os elementos
gr�ficos (widgets) da interface de usu�rio GNOME, a arquitetura GNOME
Canvas, e a vers�o GNOME da libglade.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--without-static \
	--with-gnome \
	--with-libglade
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.guile-gtk ChangeLog *.defs

%dir %{repexecdir}/gui
%dir %{repexecdir}/gui/gtk-*

%attr(755,root,root) %{repexecdir}/gui/gtk-*/gtk.so
%{repexecdir}/gui/gtk-*/gtk.la
%{repexecdir}/gui/gtk-*/types.la
%attr(755,root,root) %{repexecdir}/gui/gtk-*/types.so

%files libglade
%defattr(644,root,root,755)
%doc libglade.defs examples/test-libglade examples/simple.glade
%doc examples/rep-ui examples/rep-ui.glade
%attr(755,root,root) %{repexecdir}/gui/gtk-*/libglade.so
%{repexecdir}/gui/gtk-*/libglade.la

%files gnome
%defattr(644,root,root,755)
%doc examples/gnome-test examples/canvas-test

%attr(755,root,root) %{repexecdir}/gui/gtk-*/gnome*.so
%{repexecdir}/gui/gtk-*/gnome*.la
