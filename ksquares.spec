Name:		ksquares
Version:	4.10.0
Release:	1
Epoch:		1
Summary:	An implementation of the popular paper based game squares
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksquares/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
KSquares is an implementation of the popular paper based game squares. 
You must draw lines to complete squares, the player with the most s
quares wins.

%files
%{_kde_bindir}/ksquares
%{_kde_applicationsdir}/ksquares.desktop
%{_kde_appsdir}/ksquares
%{_kde_datadir}/config.kcfg/ksquares.kcfg
%{_kde_iconsdir}/hicolor/*/apps/ksquares.png
%{_kde_docdir}/*/*/ksquares

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

