Name: grub2
Version: 1.98
Release: alt13

Summary: GRand Unified Bootloader
License: GPL
Url: http://www.gnu.org/software/grub/grub.en.html
Group: System/Kernel and hardware
Source0: %name-%version.tar.bz2
Source1: grub2-sysconfig

Source2: 35_xen
Source3: 39_memtest
Source4: grub2.filetrigger

Patch1: grub-1.98-os-alt.patch
Patch2: grub-1.98-sysconfig-path-alt.patch
Patch3: grub-1.98-altlinux-theme.patch
Patch4: grub-1.98-evms-crap-alt.patch
Patch5: grub-1.98-debian-950-quick-boot.patch
Patch6: grub-1.98-debian-904_disable_floppies.patch

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

# Automatically added by buildreq on Sun Mar 07 2010 (-bb)
BuildRequires: fonts-bitmap-misc libfreetype-devel ruby

Exclusivearch: %ix86 x86_64

Conflicts: grub
Obsoletes: grub < %version-%release

%description
GNU GRUB is a multiboot boot loader. It was derived from GRUB. It is an
attempt to produce a boot loader for IBM PC-compatible machines that
has both the ability to be friendly to beginning or otherwise
nontechnically interested users and the flexibility to help experts in
diverse environments. It is compatible with Free/Net/OpenBSD and Linux.
It supports Win 9x/NT and OS/2 via chainloaders. It has a menu
interface and a command line interface.
It implements the Multiboot standard, which allows for flexible loading
of multiple boot images (needed for modular kernels such as the GNU
Hurd).

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
%patch5 -p1
%patch6 -p0

%build
%configure --prefix=/
%make_build

%install
%makeinstall
mkdir -p %buildroot/etc/sysconfig
install -pD -m644 %SOURCE1 %buildroot/etc/sysconfig/grub2
%find_lang grub
%buildroot/%_bindir/grub-mkfont -o %buildroot/%_datadir/grub/unifont.pf2 %_datadir/fonts/bitmap/misc/8x13.pcf.gz
install -pD -m755 %SOURCE2 %buildroot/etc/grub.d/
install -pD -m755 %SOURCE3 %buildroot/etc/grub.d/
sed -i 's,^libdir=,libdir=%_libdir,g' %buildroot/etc/grub.d/35_xen
sed -i 's,^libdir=,libdir=%_libdir,g' %buildroot/etc/grub.d/39_memtest
sed -i 's,@LOCALEDIR@,%_datadir/locale,g' %buildroot/etc/grub.d/*
mkdir -p %buildroot/%_rpmlibdir
install -pD -m755 %SOURCE4 %buildroot/%_rpmlibdir/

%files -f grub.lang
%dir %_sysconfdir/grub.d
%_sysconfdir/grub.d/00_header
%_sysconfdir/grub.d/05_altlinux_theme
%_sysconfdir/grub.d/10_linux
%_sysconfdir/grub.d/30_os-prober
%_sysconfdir/grub.d/35_xen
%_sysconfdir/grub.d/39_memtest
%config(noreplace) %_sysconfdir/grub.d/40_custom
%config(noreplace) /etc/sysconfig/grub2
%_bindir/*
%_libdir/grub
%_datadir/grub
%_sbindir/*
%_infodir/grub.info.*
%_rpmlibdir/*.filetrigger

%changelog
* Fri Jun 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt13
- update grub menu in filetrigger (ALT #23332)
- fix memtest finding

* Wed Apr 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt12
- add space before (failsafe mode) (ALT #23361)
- fix default xen initrd name

* Mon Apr 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt11
- add memtest and xen detection
- set localedir

* Fri Apr 16 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt10
- do not provide grub
- fix for evms/lvm device probing

* Mon Apr 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt9
- add 904_disable_floppies.patch from debian
- mark %_sysconfdir/grub.d/40_custom as config(noreplace)
- add Provides/Obsoletes for grub

* Tue Mar 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt8
- add 950-quick-boot.patch from debian
- enable savedefault feature by default

* Mon Mar 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt7
- remove evms crap in one more place

* Fri Mar 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt6
- make evms-crap-alt patch more common

* Fri Mar 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt5
- rewrite stupid evms-crap-alt patch

* Thu Mar 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt4
- remove evms crap (for installer)

* Tue Mar 09 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt3
- fix bug in default menuentries

* Mon Mar 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt2
- boot default (/boot/vmlinuz) kernel first
- change default font to 8x13

* Sat Mar 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt1
- 1.98

* Sat Jan 30 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.97-alt3
- 1.97.2

* Thu Jan 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.97-alt2
- add patches from fedora (initramfs,os name)
- remove buggy grub2-helper-10_altlinux
- make /etc/sysconfig/grub2 useful

* Mon Jan 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.97-alt1
- 1.97

* Fri Jun 19 2009 Denis Kuznetsov <dek@altlinux.ru> 1.96-alt2
- Fixed #20475

* Thu Jun 11 2009 Denis Kuznetsov <dek@altlinux.ru> 1.96-alt1
- Initial build for Sisyphus

