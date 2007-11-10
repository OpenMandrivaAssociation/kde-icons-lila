%define base_name	kde-icons
%define theme_name	lila
%define version		0.7.1
%define name		%{base_name}-%{theme_name}
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Lila icons for KDE Desktop
License:	GPL
Group:		Graphical desktop/KDE
Source:		%{theme_name}-%{version}.tar.bz2
URL:		http://kde-look.org/content/show.php?content=11492
Requires:	kdebase kdegraphics-ksvg
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

