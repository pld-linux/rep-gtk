Summary:	GTK+ binding for librep Lisp environment
Summary(es.UTF-8):	Conjuntos de componentes GTK+ para el ambiente LISP librep
Summary(ko.UTF-8):	librep Lisp 환경을 위한 GTK+ 바인딩
Summary(pl.UTF-8):	Interfejs GTK+ do środowiska Lispa librep
Summary(pt_BR.UTF-8):	Conjuntos de componentes GTK+ para o ambiente LISP librep
Name:		rep-gtk
Version:	0.18
Release:	3
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/rep-gtk/%{name}-%{version}.tar.gz
# Source0-md5:	220b0d728656472c068e40823f0a3b22
Patch0:		rep-gdkcolor.patch
Patch1:		%{name}-gtk2.10.patch
%define		repexecdir	%(rep-config --execdir 2>/dev/null || echo ERROR)
URL:		http://rep-gtk.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.3
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.1
BuildRequires:	libgnomecanvas-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	librep-devel >= 0.16
BuildRequires:	pkgconfig
Requires:	%{repexecdir}
Requires:	libgnomeui >= 2.3.3.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}

%description
This is a binding of GTK+ for the librep Lisp interpreter. It is based
on Marius Vollmer's guile-gtk package with a new glue-code generator.

%description -l es.UTF-8
Este paquete contiene un conjunto de componentes GTK+ para el
interpretador LISP librep. Se basa en el paquete guile-gtk, con un
nuevo generador de código intermediario.

%description -l pl.UTF-8
To jest interfejs GTK+ do interpretera Lispa librep. Bazuje na
pakiecie guile-gtk Mariusa Vollmera z nowym generatorem kodu.

%description -l pt_BR.UTF-8
Esse pacote contém um conjunto de componentes GTK+ para o
interpretador LISP librep. Ele é baseado no pacote guile-gtk, com um
novo gerador de código intermediário.

%package libglade
Summary:	librep binding for the libglade library for loading user interfaces
Summary(ko.UTF-8):	사용자 인터페이스를 읽어들이기 위한 libglade라이브러리의 librep 바인딩
Summary(pl.UTF-8):	Interfejs librep do biblioteki libglade
Summary(pt_BR.UTF-8):	Vínculos librep para a biblioteca libglade para carregamento de interfaces de usuário
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description libglade
This is a binding of libglade for the librep Lisp interpreter.
libglade allows applications to dynamically load XML descriptions of
GTK+ widget hierarchies. These hierarchies may be created by the GLADE
GUI builder.

%description libglade -l pl.UTF-8
To jest interfejs libglade do interpretera Lispa librep. libglade
pozwala aplikacjom dynamicznie wczytywać opisy XML hierarchii widgetów
GTK+.

%description libglade -l pt_BR.UTF-8
Este é um bind da libglade para o interpretador librep Lisp. A
libglade permite que as aplicações carreguem dinamicamente as
descrições XML das hierarquias de elementos gráficos (widgets) GTK+.
Essas hierarquias podem ser criadas com o GLADE GUI builder.

%package gnome
Summary:	GNOME binding for librep
Summary(ko.UTF-8):	librep를 위한 GNOME바인딩
Summary(pl.UTF-8):	Interfejs GNOME do librep
Summary(pt_BR.UTF-8):	GNOME binding for librep
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnome
This is a binding of the various GNOME libraries for the librep Lisp
interpreter. It include support for the basic GNOME functions, the
GNOME user interface widgets, and the GNOME Canvas architecture.

%description gnome -l pl.UTF-8
To jest interfejs różnych bibliotek GNOME do interpretera Lispa
librep. Zawiera wsparcie dla podstawowych funkcji GNOME, widgetów
interfejsu użytkownika GNOME, architektury GNOME Canvas.

%description gnome -l pt_BR.UTF-8
Este é um bind das várias bibliotecas GNOME para o interpretador
librep Lisp. Inclui suporte às funções básicas do GNOME, os elementos
gráficos (widgets) da interface de usuário GNOME, a arquitetura GNOME
Canvas, e a versão GNOME da libglade.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--disable-static \
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
%attr(755,root,root) %{repexecdir}/gui/gtk-*/types.so
%{repexecdir}/gui/gtk-*/types.la

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
