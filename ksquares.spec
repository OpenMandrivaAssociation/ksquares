%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		ksquares
Version:	21.08.0
Release:	1
Epoch:		1
Summary:	An implementation of the popular paper based game squares
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksquares/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DocTools)

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
#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
