Summary:	KDE front-end to Cscope
Summary(pl):	Interfejs KDE do Cscope
Name:		kscope
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/kscope/%{name}-%{version}.tar.gz
# Source0-md0:	7a273bca1ed74abd1e1e83224c283eb8
URL:		http://kscope.sourceforge.net/
BuildRequires:	kdebase-devel
Requires:	cscope
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
KScope to interfejs KDE do Cscope. Daje �rodowisko do edycji �r�de�
dla du�ych projekt�w w C, jak na przyk�ad j�dro Linuksa. KScope nie ma
by� zamiennikiem dla �adnego z wiod�cych IDE dla Linuksa/KDE, takich
jak KDevelop. Mimo wszystko, te IDE, cz�sto przeznaczone do
programowania zorientowanego obiektowo, w przestrzeni u�ytkownika,
zwykle nie pasuj� do utrzymywania du�ych projekt�w, u�ywaj�cych
programowania funkcyjnego. Na przyk�ad, u�ywanie okna "Klasy" do
wy�wietlania tysi�cy funkcji z j�dra Linuksa, by�oby niepraktyczne, i
przeszkadza�oby w u�ytecznej nawigacji po kodzie. KScope, z drugiej
strony, dostarcza raczej przydatny mechanizm do nawigacji po kodzie,
pozwalaj�c u�ytkownikowi wykonywa� zapytania na kodzie.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	shelldesktopdir=%{_desktopdir} \
	kde_htmldir=%{_kdedocdir} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_iconsdir}/*/*/*/*.png
%{_desktopdir}/*.desktop
