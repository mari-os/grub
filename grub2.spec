Name: grub2
Version: 1.98
Release: alt1

Summary: GRand Unified Bootloader
License: GPL
Url: http://www.gnu.org/software/grub/grub.en.html
Group: System/Kernel and hardware
Source0: %name-%version.tar.bz2
Source1: grub2-sysconfig
Patch1: grub-1.97.1-initramfs.patch
Patch2: grub-1.97-os-alt.patch
Patch3: grub-1.97-sysconfig-path-alt.patch

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

# Automatically added by buildreq on Wed Jun 10 2009 (-bb)
BuildRequires: genisoimage libgoogle-perftools liblzo-devel ruby

Conflicts:  grub

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

%build
%configure --prefix=/
%make_build

%install
%makeinstall
mkdir -p %buildroot/etc/sysconfig
install -pD -m644 %SOURCE1 %buildroot/etc/sysconfig/grub2

%files
/etc/grub.d
%config(noreplace) /etc/sysconfig/grub2
%_bindir/*
%_libdir/grub
%_sbindir/*
%_infodir/grub.info.*

%changelog
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

