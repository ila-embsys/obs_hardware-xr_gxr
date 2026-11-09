#
# spec file for package gxr
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define _libver 0.16

Name:           gxr
Version:        0.16.0
Release:        0
Summary:        A glib wrapper for the OpenVR and soon the OpenXR API
License:        MIT
Url:            https://gitlab.freedesktop.org/xrdesktop/gxr
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2#/%{name}-%{version}.tar.bz2
Patch0:         0000_add_gxr_context_wait_frame.patch
Patch1:         0001_set_initial_predicted_display_time_to_non_zero.patch
Patch2:         0002_use_gtk4_dep.patch
BuildRequires:  meson >= 0.52
BuildRequires:  libstdc++-devel
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig(gtk4) >= 4.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gulkan-0.16) >= 0.16.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(openxr)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
A glib wrapper for the OpenVR and soon the OpenXR API.

%package -n typelib-1_0-Gxr-0_16
Summary:        Introspection bindings for the Gxr library
Group:          System/Libraries

%description -n typelib-1_0-Gxr-0_16
This package provides the GObject Introspection bindings for Gxr.

%package devel
Summary:        A glib wrapper for the OpenVR and soon the OpenXR API
Requires:       %{name} = %{version}
Requires:       typelib-1_0-Gxr-0_16 = %{version}

%description devel
A glib wrapper for the OpenVR and soon the OpenXR API.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
export SUSE_ASNEEDED=0
%meson -Dintrospection=true
%meson_build

%install
export SUSE_ASNEEDED=0
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%{_bindir}/%{name}-demo
%{_libdir}/lib%{name}-%{_libver}.so.*

%files devel
%dir %{_includedir}/%{name}-%{_libver}
%{_includedir}/%{name}-%{_libver}/*.h
%{_libdir}/pkgconfig/%{name}-%{_libver}.pc
%{_libdir}/lib%{name}-%{_libver}.so
%{_datadir}/gir-1.0/*.gir

%files -n typelib-1_0-Gxr-0_16
%{_libdir}/girepository-1.0/Gxr-0.16.typelib

%changelog
