Summary:	KDE front-end to Cscope
Summary(pl.UTF-8):   Interfejs KDE do Cscope
Name:		kscope
Version:	1.4.2
Release:	1
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/kscope/%{name}-%{version}.tar.gz
# Source0-md5:	21749b587ce4167758e8173bde89670d
URL:		http://kscope.sourceforge.net/
BuildRequires:	automake
BuildRequires:	graphviz-devel >= 2.6-3
BuildRequires:	kdebase-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	cscope
Requires:	ctags
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KScope is a KDE front-end to Cscope. It provides a source-editing
environment for large C projects, such as the Linux kernel. KScope is
by no means intended to be a replacement to any of the leading
Linux/KDE IDEs, such as KDevelop. However, these IDEs, often targeted
at Object-Oriented, user-space programming, are usually unsuitable for
maintaining large projects, using functional programming. For
instance, using a "Classes" window to display the thousands of
functions in the Linux kernel code, would be impractical, and thus
will prevent any useful navigation throughout the code. KScope, on the
other hand, provides a rather useful mechanism for code-navigation, by
allowing the user to run queries on the code.

%description -l pl.UTF-8
KScope to interfejs KDE do Cscope. Daje środowisko do edycji źródeł
dla dużych projektów w C, jak na przykład jądro Linuksa. KScope nie ma
być zamiennikiem dla żadnego z wiodących IDE dla Linuksa/KDE, takich
jak KDevelop. Mimo wszystko, te IDE, często przeznaczone do
programowania zorientowanego obiektowo, w przestrzeni użytkownika,
zwykle nie pasują do utrzymywania dużych projektów, używających
programowania funkcyjnego. Na przykład, używanie okna "Klasy" do
wyświetlania tysięcy funkcji z jądra Linuksa, byłoby niepraktyczne, i
przeszkadzałoby w użytecznej nawigacji po kodzie. KScope, z drugiej
strony, dostarcza całkiem przydatny mechanizm do nawigacji po kodzie,
pozwalając użytkownikowi wykonywać zapytania na kodzie.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	shelldesktopdir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_iconsdir}/hicolor/*/*/*.png
%{_desktopdir}/kde/*.desktop
