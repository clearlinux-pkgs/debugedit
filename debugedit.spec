#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC57E3CCACD99A78 (mjw@gnu.org)
#
Name     : debugedit
Version  : 5.0
Release  : 95
URL      : https://sourceware.org/ftp/debugedit/5.0/debugedit-5.0.tar.xz
Source0  : https://sourceware.org/ftp/debugedit/5.0/debugedit-5.0.tar.xz
Source1  : https://sourceware.org/ftp/debugedit/5.0/debugedit-5.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1
Requires: debugedit-bin = %{version}-%{release}
Requires: debugedit-license = %{version}-%{release}
Requires: debugedit-man = %{version}-%{release}
BuildRequires : help2man
BuildRequires : pkgconfig(libdw)
BuildRequires : pkgconfig(libelf)
BuildRequires : sed
BuildRequires : util-linux
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
%setup -q -n debugedit-5.0
cd %{_builddir}/debugedit-5.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
## build_prepend content
sed -i 's/\$LDFLAGS//' tests/testsuite
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631342689
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1631342689
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/debugedit
cp %{_builddir}/debugedit-5.0/COPYING %{buildroot}/usr/share/package-licenses/debugedit/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/debugedit-5.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/debugedit/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/debugedit-5.0/COPYING3 %{buildroot}/usr/share/package-licenses/debugedit/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
