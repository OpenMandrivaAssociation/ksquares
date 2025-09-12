#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		ksquares
Version:	25.08.1
Release:	%{?git:0.%{git}.}1
Summary:	An implementation of the popular paper based game squares
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/ksquares/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/ksquares/-/archive/%{gitbranch}/ksquares-%{gitbranchd}.tar.bz2#/ksquares-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ksquares-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KDEGames6)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DocTools)

%rename plasma6-ksquares

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KSquares is an implementation of the popular paper based game squares. 
You must draw lines to complete squares, the player with the most s
quares wins.

%files -f %{name}.lang
%{_bindir}/ksquares                                                                                    
%{_datadir}/applications/org.kde.ksquares.desktop                                                                                                                                
%{_datadir}/config.kcfg/ksquares.kcfg      
%{_iconsdir}/hicolor/*/apps/ksquares.png                                                               
%{_datadir}/metainfo/org.kde.ksquares.appdata.xml
