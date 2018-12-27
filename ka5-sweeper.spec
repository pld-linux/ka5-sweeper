%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		sweeper
Summary:	sweeper
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	91f60a074c3bc1359fb3e32a86f20d2c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kactivities-stats-devel >= 5.23.0
BuildRequires:	kf5-kbookmarks-devel >= 5.23.0
BuildRequires:	kf5-kconfig-devel >= 5.23.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.23.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.23.0
BuildRequires:	kf5-kcrash-devel >= 5.23.0
BuildRequires:	kf5-kdoctools-devel >= 5.23.0
BuildRequires:	kf5-ki18n-devel >= 5.23.0
BuildRequires:	kf5-kio-devel >= 5.23.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.23.0
BuildRequires:	kf5-kxmlgui-devel >= 5.23.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sweeper helps to clean unwanted traces the user leaves on the system
and to regain disk space removing unused temporary files.

Features

- It can remove web-related traces: cookies, history, cache
- It can remove the image thumbnails cache
- It can also clean the applications and documents history

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sweeper
%{_desktopdir}/org.kde.sweeper.desktop
%{_datadir}/dbus-1/interfaces/org.kde.sweeper.xml
%{_datadir}/kxmlgui5/sweeper
%{_datadir}/metainfo/org.kde.sweeper.appdata.xml
