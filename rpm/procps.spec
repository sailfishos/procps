Summary: System and process monitoring utilities
Name: procps
Version: 3.3.15
Release: 1
License: GPLv2+ and LGPLv2+
URL: https://gitlab.com/procps-ng/procps
Source0: %{name}-%{version}.tar.gz
Source1: ipv4.sysctl
Source2: sysrq.sysctl
Source3: vm.sysctl

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

# enable core dump generation
Patch1: procps-enable-core.patch

BuildRequires: ncurses-devel
BuildRequires: autoconf, gettext
BuildRequires: pkgconfig(libsystemd)

%description
The procps package contains a set of system utilities that provide
system information. Procps includes ps, free, skill, pkill, pgrep,
snice, tload, top, uptime, vmstat, w, watch and pdwx. The ps command
displays a snapshot of running processes. The top command provides
a repetitive update of the statuses of running processes. The free
command displays the amounts of free and used memory on your
system. The skill command sends a terminate command (or another
specified signal) to a specified set of processes. The snice
command is used to change the scheduling priority of specified
processes. The tload command prints a graph of the current system
load average to a specified tty. The uptime command displays the
current time, how long the system has been running, how many users
are logged on, and system load averages for the past one, five,
and fifteen minutes. The w command displays a list of the users
who are currently logged on and what they are running. The watch
program watches a running program. The vmstat command displays
virtual memory statistics about processes, memory, paging, block
I/O, traps, and CPU activity. The pwdx command reports the current
working directory of a process or processes.

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package doc
Summary:  Documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.

%prep
%setup -q -n %{name}-%{version}/upstream

%patch1 -p1

%build
echo "%{version}" > .tarball-version
./autogen.sh
autoreconf --verbose --force --install

%configure \
           --exec-prefix=/ \
           --docdir=%{_docdir}/%{name}-%{version} \
           --disable-static \
           --disable-w-from \
           --disable-kill \
           --disable-pidof \
           --enable-watch8bit \
           --enable-skill \
           --enable-sigwinch \
           --with-systemd \
           --disable-modern-top

make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/%{_sysconfdir}/sysctl.d
install -m0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/sysctl.d/00-ipv4.conf
install -m0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/sysctl.d/00-sysrq.conf
install -m0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysctl.d/00-vm.conf

# copy doc files to their directory
install -m0644 -t %{buildroot}/%{_docdir}/%{name}-%{version}/ \
        AUTHORS NEWS README.md top/README.top

%find_lang %{name}-ng

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}-ng.lang
%defattr(-,root,root,-)
%license COPYING COPYING.LIB
%{_libdir}/lib%{name}.so.*
%{_bindir}/*
%{_sbindir}/sysctl
%config %{_sysconfdir}/sysctl.d

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.la
%{_includedir}/proc
%{_libdir}/pkgconfig/lib%{name}.pc

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
%{_mandir}/man*/*
