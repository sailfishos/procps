#specfile originally created for Fedora, modified for Moblin Linux
Summary: System and process monitoring utilities
Name: procps
Version: 3.2.8
Release: 1
License: GPLv2+ and LGPLv2+
Group: Applications/System
URL: http://procps.sourceforge.net
Source: http://procps.sourceforge.net/procps-%{version}.tar.gz
Source1: FAQ
Source2: ipv4.sysctl
Source3: sysrq.sysctl
Source4: vm.sysctl
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Patch1: procps-3.2.7-selinux.patch
Patch2: procps-3.1.15-misc.patch
Patch3: procps-3.2.3-FAQ.patch
Patch4: procps-3.2.1-selinux-workaround.patch
Patch6: procps-3.2.3-noproc.patch
Patch7: procps-3.2.3-pseudo.patch
Patch8: procps-3.2.4-0x9b.patch
# 157725 - sysctl -A returns an error
Patch9: procps-3.2.5-sysctl-writeonly.patch
# 161449 - "top" ignores user and system toprc
Patch10: procps-3.2.5-top-rc.patch
# 161303 - 'top' failed when remove cpus
# 186017 - Top "Cpu0" line never updates on single processor machine
Patch11: procps-3.2.7-top-remcpu.patch
# Selinux
Patch12: procps-3.2.6-libselinux.patch
# 177453 - for VIRT use proc->vm_size rather then proc->size (workaround)
Patch13: procps-3.2.6-top-env-vmsize.patch
# 174619 - workaround for reliable Cpu(s) data in the first loop
Patch14: procps-3.2.6-top-env-cpuloop.patch
# 185299 - cpu steal time support
Patch15: procps-3.2.7-vmstat-cpusteal.patch
# 134516 - ps ignores /proc/#/cmdline if contents 2047 bytes
Patch16: procps-3.2.7-longcmd.patch
# 189349 - 32bit vmstat on 64bit kernel
Patch17: procps-3.2.7-vmstat-pgpg.patch
# 212637 - sysctl using deprecated syscall
# 228870 - process `sysctl' is using deprecated sysctl ...
Patch18: procps-3.2.7-sysctl-ignore.patch
# 140975 - top corrupts screen when sorting on first column
Patch19: procps-3.2.7-top-sorthigh.path
# 234546 - 'w' doesn't give correct information about what's being run.
Patch20: procps-3.2.7-w-best.patch
# 183029 - watch ignores unicode characters
Patch21: procps-3.2.7-watch-unicode.patch
# 222251 - STIME can jitter by one second
Patch22: procps-3.2.7-ps-stime.patch
#244152 - ps truncates eip and esp to 32-bit values on 64-bit systems
Patch23: procps-3.2.7-ps-eip64.patch
#244960 - ps manpage formatted incorrectly
Patch24: procps-3.2.7-psman.patch
#255441 - ldopen libselinux.so.1 instead of libselinux.so
Patch25: procps-3.2.7-ps-libselinux.patch
#185994 - error when using "Single Cpu = Off" option
Patch26: procps-3.2.7-top-cpu0.patch
#354001 - CPU value in top is reported as an integer
Patch27: procps-3.2.7-top-cpuint.patch
#296471 - update top man page
Patch28: procps-3.2.7-top-manpage.patch
# Fix build error when there is LD_AS_NEEDED
Patch29: fix-makefile-error-with-as-needed.patch
#440694 - strange text after selecting few field
Patch30: procps-3.2.7-top-clrscr.patch
#435453 - errors with man -t formatting of ps man page
Patch31: procps-3.2.7-ps-man-fmt.patch
#472783 - 'vmstat -p <partition name>', 
# the detailed statistics of the partition name is not output.
Patch32: procps-3.2.7-vmstat-partstats-long.patch
# Fix vmstat header to be 80 chars not 81
Patch33: procps-3.2.7-vmstat-header.patch
# rhel bug #475963: slabtop -o should display the info once
Patch34: procps-3.2.7-slabtop-once.patch
#476134 - added timestamp to vmstat with new option -t
Patch35: procps-3.2.7-vmstat-timestamp.patch
#manual page updated to document the -t functionality
Patch36: procps-3.2.7-vmstat-timestamp-manpage.patch
# 'requested writes' display in partition statistics
Patch37: procps-3.2.7-vmstat-partstats-reqwrites.patch
# '-l' option of 'free' documented
Patch38: procps-3.2.7-free-hlmem.patch
# enable core dump generation
Patch39: procps-enable-core.patch
# fix "Unknown HZ value! (??) Assume 100." issue
Patch40: unknown-hz-value-fix.patch

BuildRequires: ncurses-devel

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

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1

cp %SOURCE1 .

%build
make SHARED=1 CFLAGS="$RPM_OPT_FLAGS" W_SHOWFROM=-DW_SHOWFROM lib64=%{_lib}

%install
rm -rf %{buildroot}
make ldconfig=true DESTDIR=%{buildroot} lib64=%{_lib} install="install -D" \
	SKIP="/bin/kill /usr/share/man/man1/kill.1" install
mkdir -p %{buildroot}/%{_docdir}/procps-%{version}
# keep 'rpm' happy...
chmod -R u+w %{buildroot}/sbin
chmod -R u+w %{buildroot}/bin
chmod -R u+w %{buildroot}/usr/bin
chmod -R u+w %{buildroot}/lib*
mkdir -p %{buildroot}/%{_sysconfdir}/sysctl.d
install -m0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/sysctl.d/ipv4.conf
install -m0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysctl.d/sysrq.conf
install -m0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sysctl.d/vm.conf

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(0644,root,root,755)
%doc NEWS BUGS TODO FAQ
%attr(755,root,root) /%{_lib}/*
%attr(755,root,root) /bin/ps
%attr(755,root,root) /sbin/sysctl
%attr(755,root,root) /usr/bin/*
%{_sysconfdir}/sysctl.d
%{_sysconfdir}/sysctl.d/*

%doc %attr(0644,root,root) %{_mandir}/man1/*
%doc %attr(0644,root,root) %{_mandir}/man8/*
%doc %attr(0644,root,root) %{_mandir}/man5/*

