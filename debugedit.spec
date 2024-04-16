#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xFC57E3CCACD99A78 (mjw@gnu.org)
#
Name     : debugedit
Version  : 5.0
Release  : 96
URL      : https://sourceware.org/ftp/debugedit/5.0/debugedit-5.0.tar.xz
Source0  : https://sourceware.org/ftp/debugedit/5.0/debugedit-5.0.tar.xz
Source1  : https://sourceware.org/ftp/debugedit/5.0/debugedit-5.0.tar.xz.sig
Source2  : FC57E3CCACD99A78.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1
Requires: debugedit-bin = %{version}-%{release}
Requires: debugedit-license = %{version}-%{release}
Requires: debugedit-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gnupg
BuildRequires : help2man
BuildRequires : pkgconfig(libdw)
BuildRequires : pkgconfig(libelf)
BuildRequires : sed
BuildRequires : util-linux
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-32bit-kernel-builds-by-not-using-eu-strip.patch
Patch2: 0002-Relocate-debuginfo-to-usr-share-debug.patch
Patch3: 0003-debuginfo-do-not-strip-static-libraries.patch
Patch4: 0004-scripts-Don-t-bail-out-when-debugedit-fails.patch
Patch5: 0005-Don-t-fail-a-build-if-build-id-is-a-duplicate.patch
Patch6: 0006-preserve-timestamps.patch

%description
DEBUGEDIT
The debugedit project provides programs and scripts for creating
debuginfo and source file distributions, collect build-ids and rewrite
source paths in DWARF data for debugging, tracing and profiling.

%package bin
Summary: bin components for the debugedit package.
Group: Binaries
Requires: debugedit-license = %{version}-%{release}

%description bin
bin components for the debugedit package.


%package license
Summary: license components for the debugedit package.
Group: Default

%description license
license components for the debugedit package.


%package man
Summary: man components for the debugedit package.
Group: Default

%description man
man components for the debugedit package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) FC57E3CCACD99A78' gpg.status
%setup -q -n debugedit-5.0
cd %{_builddir}/debugedit-5.0
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
pushd ..
cp -a debugedit-5.0 buildavx2
popd

%build
## build_prepend content
sed -i 's/\$LDFLAGS//' tests/testsuite
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713277356
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
sed -i 's/\$LDFLAGS//' tests/testsuite
## build_prepend end
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713277356
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/debugedit
cp %{_builddir}/debugedit-%{version}/COPYING %{buildroot}/usr/share/package-licenses/debugedit/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/debugedit-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/debugedit/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/debugedit-%{version}/COPYING3 %{buildroot}/usr/share/package-licenses/debugedit/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/debugedit
/V3/usr/bin/sepdebugcrcfix
/usr/bin/debugedit
/usr/bin/find-debuginfo
/usr/bin/sepdebugcrcfix

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/debugedit/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
/usr/share/package-licenses/debugedit/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/debugedit/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/debugedit.1
/usr/share/man/man1/find-debuginfo.1
/usr/share/man/man1/sepdebugcrcfix.1
