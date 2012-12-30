Name:           xhost
Version:        1.0.5
Release:        0
License:        MIT
Summary:        Utility to control X server access
Url:            http://xorg.freedesktop.org/
Group:          System/X11
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
xhost is used to manage the list of host names or user names
allowed to make connections to the X server.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/xhost
%{_mandir}/man1/xhost.1%{?ext_man}

%changelog
