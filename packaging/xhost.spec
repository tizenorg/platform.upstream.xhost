%bcond_with x

Name:           xhost
Version:        1.0.6
Release:        0
License:        MIT
Summary:        Utility to control X server access
Url:            http://xorg.freedesktop.org/
Group:          System/X11
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1001: 	xhost.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%if !%{with x}
ExclusiveArch:
%endif

%description
xhost is used to manage the list of host names or user names
allowed to make connections to the X server.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_bindir}/xhost
%{_mandir}/man1/xhost.1%{?ext_man}

%changelog
