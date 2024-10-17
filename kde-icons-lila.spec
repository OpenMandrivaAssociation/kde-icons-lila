%define base_name	kde-icons
%define theme_name	lila
%define version		0.7.1
%define name		%{base_name}-%{theme_name}
%define release %mkrel 9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Lila icons for KDE Desktop
License:	GPL
Group:		Graphical desktop/KDE
Source:		%{theme_name}-%{version}.tar.bz2
URL:		https://kde-look.org/content/show.php?content=11492
Requires:	kdebase3-progs 
Requires:   kdegraphics3-ksvg
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Lila is a port of a GNOME theme, also called Lila, that can be found here:
http://programmer-art.org/index.php?page=gentoo
The package contains PNG & SVG icons and a colour scheme.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{theme_name}

%build
find -type f -exec chmod 644 {} \;

%install
install -d -m 755 %buildroot%_iconsdir/%{theme_name}-%{version}
install -d -m 755 %buildroot%_iconsdir/%{theme_name}-%{version}/16x16
install -d -m 755 %buildroot%_iconsdir/%{theme_name}-%{version}/32x32
install -d -m 755 %buildroot%_iconsdir/%{theme_name}-%{version}/48x48
install -d -m 755 %buildroot%_iconsdir/%{theme_name}-%{version}/64x64
install -d -m 755 %buildroot%_iconsdir/%{theme_name}-%{version}/128x128
install -d -m 755 %buildroot/%{_datadir}/apps/kdisplay/color-schemes/
install -m 644 lila.kcsrc %buildroot/%_datadir/apps/kdisplay/color-schemes/ 
cp -fr * %buildroot%_iconsdir/%{theme_name}-%{version}/
cp -f 16x16/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}-%{version}/16x16/apps/menuk-mdk.png
cp -f 16x16/apps/icons.png %buildroot%_iconsdir/%{theme_name}-%{version}/16x16/apps/desktop-mdk.png
cp -f 16x16/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}-%{version}/16x16/apps/home-mdk.png
cp -f 32x32/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}-%{version}/32x32/apps/menuk-mdk.png
cp -f 32x32/apps/icons.png %buildroot%_iconsdir/%{theme_name}-%{version}/32x32/apps/desktop-mdk.png
cp -f 32x32/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}-%{version}/32x32/apps/home-mdk.png
cp -f 48x48/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}-%{version}/48x48/apps/menuk-mdk.png
cp -f 48x48/apps/icons.png %buildroot%_iconsdir/%{theme_name}-%{version}/48x48/apps/desktop-mdk.png
cp -f 48x48/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}-%{version}/48x48/apps/home-mdk.png
cp -f 64x64/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}-%{version}/64x64/apps/menuk-mdk.png
cp -f 64x64/apps/icons.png %buildroot%_iconsdir/%{theme_name}-%{version}/64x64/apps/desktop-mdk.png
cp -f 64x64/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}-%{version}/64x64/apps/home-mdk.png
cp -f 128x128/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}-%{version}/128x128/apps/menuk-mdk.png
cp -f 128x128/apps/icons.png %buildroot%_iconsdir/%{theme_name}-%{version}/128x128/apps/desktop-mdk.png
cp -f 128x128/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}-%{version}/128x128/apps/home-mdk.png


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYRIGHT CREDITS LICENSE
%_iconsdir/%{theme_name}-%{version}/*
%_datadir/apps/kdisplay/color-schemes/*.kcsrc



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-9mdv2011.0
+ Revision: 619898
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.7.1-8mdv2010.0
+ Revision: 438080
- rebuild

* Sun Mar 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.7.1-7mdv2009.1
+ Revision: 360334
- Fix Requires

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.7.1-6mdv2009.0
+ Revision: 247603
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.7.1-4mdv2008.1
+ Revision: 107278
- Fix Requires (kdebase-progs is a better require)
- import kde-icons-lila


* Tue Jul 11 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.7.1-3mdv2007.0
- Rebuild for new extension
- use mkrel

*Wed Mar 23 2005 Sebastien Savarin <plouf@mandrake.org> 0.7.1-2mdk
-rename icons kmenu.png > menuk-mdk.png kfm_home.png > home-mdk.png
 icons.png > desktop-mdk.png at build

* Tue Jan 25 2005 Laurent Culioli <laurent@mandrake.org> 0.7.1-1mdk
-new version

* Sun May 02 2004 Laurent Culioli <laurent@mandrake.org> 0.7-1mdk
- 0.7

* Mon Apr 19 2004 Laurent Culioli <laurent@mandrake.org> 0.6-1mdk
- new kde icon theme
