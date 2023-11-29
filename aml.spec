%define major 0
%define libname %mklibname aml
%define devname %mklibname aml -d

Name: aml
Version: 0.3.0
Release: 2
Source0: https://github.com/any1/aml/archive/refs/tags/v%{version}.tar.gz
Summary: Event loop handling library developed for Wayland VNC servers
URL: https://github.com/any1/aml
License: ISC
Group: System/Libraries
BuildRequires: meson
BuildRequires: ninja

%description
AML (Another Main Loop) is an event loop handling library developed for
Wayland VNC servers.

Goals:
 * Portability
 * Utility
 * Simplicity

Non-goals:
 * MS Windows (TM) support
 * Solving the C10K problem

Features:
 * File descriptor event handlers
 * Timers
 * Tickers
 * Signal handlers
 * Idle dispatch callbacks
 * Thread pool
 * Interoperability with other event loops

%package -n %{libname}
Summary: Event loop handling library developed for Wayland VNC servers
Group: System/Libraries

%description -n %{libname}
%{description}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%meson

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
