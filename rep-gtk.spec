Summary:	GTK+ binding for librep Lisp environment
Name:		rep-gtk
Version:	0.5
Release:	1
Requires:	librep >= 0.4, gtk+ >= 1.2
License:	GPL
Group:		Development/Languages
Source:		ftp.dcs.warwick.ac.uk:/people/John.Harper/librep/rep-gtk-%{ver}.tar.gz
URL:		http://www.dcs.warwick.ac.uk/~john/sw/rep-gtk.html
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is a binding of GTK+ for the librep Lisp interpreter. It is based
on Marius Vollmer's guile-gtk package (initially version 0.15, updated
to 0.16), with a new glue-code generator.

%prep
%setup -q

%build
./configure --prefix %{_prefix} %{_host}
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install \
    installdir=$RPM_BUILD_ROOT%{_prefix}/libexec/rep/%{_host}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README README.guile-gtk ChangeLog gtk-1.2.defs gdk-1.2.defs
%{_prefix}/libexec/rep/%{_host}/libgtk.so*
%{_prefix}/libexec/rep/%{_host}/libgtk.la
