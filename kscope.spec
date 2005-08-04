Summary:	KDE front-end to Cscope
Summary(pl):	Interfejs KDE do Cscope
Name:		kscope
Version:	1.3.0
Release:	1
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/kscope/%{name}-%{version}.tar.gz
# Source0-md5:	1b593c109b59bd65345d0bf9339ff674
Patch0:		%{name}-desktop.patch
URL:		http://kscope.sourceforge.net/
BuildRequires:	automake
BuildRequires:	graphviz-devel
BuildRequires:	kdebase-devel
BuildRequires:	libsvg-cairo-devel
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

%description -l pl
KScope to interfejs KDE do Cscope. Daje ¶rodowisko do edycji ¼róde³
dla du¿ych projektów w C, jak na przyk³ad j±dro Linuksa. KScope nie ma
byæ zamiennikiem dla ¿adnego z wiod±cych IDE dla Linuksa/KDE, takich
jak KDevelop. Mimo wszystko, te IDE, czêsto przeznaczone do
programowania zorientowanego obiektowo, w przestrzeni u¿ytkownika,
zwykle nie pasuj± do utrzymywania du¿ych projektów, u¿ywaj±cych
programowania funkcyjnego. Na przyk³ad, u¿ywanie okna "Klasy" do
wy¶wietlania tysiêcy funkcji z j±dra Linuksa, by³oby niepraktyczne, i
przeszkadza³oby w u¿ytecznej nawigacji po kodzie. KScope, z drugiej
strony, dostarcza ca³kiem przydatny mechanizm do nawigacji po kodzie,
pozwalaj±c u¿ytkownikowi wykonywaæ zapytania na kodzie.

%prep
%setup -q
%patch0 -p1

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
