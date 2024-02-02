%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		plasma6-ksquares
Version:	24.01.95
Release:	1
Summary:	An implementation of the popular paper based game squares
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksquares/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ksquares-%{version}.tar.xz
BuildRequires:	libkdegames-devel
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

%description
KSquares is an implementation of the popular paper based game squares. 
You must draw lines to complete squares, the player with the most s
quares wins.

%files -f ksquares.lang
%{_bindir}/ksquares                                                                                    
%{_datadir}/applications/org.kde.ksquares.desktop                                                                                                                                
%{_datadir}/config.kcfg/ksquares.kcfg      
%{_iconsdir}/hicolor/*/apps/ksquares.png                                                               
%{_datadir}/metainfo/org.kde.ksquares.appdata.xml
#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n ksquares-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang ksquares --with-html
