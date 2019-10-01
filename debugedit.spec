Name:           debugedit
Version:        4.14.2.1
Release:        89
License:        LGPL-2.1
Summary:        The RPM package management system
Url:            http://rpm.org/
Group:          base
Source0:        http://ftp.rpm.org/releases/rpm-4.14.x/rpm-4.14.2.1.tar.bz2


BuildRequires:  bzip2-dev
BuildRequires:  db-dev
BuildRequires:  elfutils-dev
BuildRequires:  file-dev
BuildRequires:  acl-dev
BuildRequires:  attr-dev
BuildRequires:  nss-dev nspr-dev
BuildRequires:  libstdc++-dev
BuildRequires:  openssl-dev
BuildRequires:  python3-core
BuildRequires:  xz-dev
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  popt-dev
BuildRequires:	gettext 
BuildRequires:  automake automake-dev
BuildRequires:  libtool-dev
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  libtool autoconf m4 gettext-dev autoconf pkg-config-dev
BuildRequires:	bison flex
BuildRequires:  python3-dev

Requires: zip unzip debugedit-bin


%description
The RPM package management system.

%package bin
License:        LGPL-2.1
Summary:        Translations for the rpm package
Group:          libs

%description bin
Debugedit binary

%package lib
License:        LGPL-2.1
Summary:        debugedit helper lib
Group:          libs

%description lib
Debugedit helper lib

%prep
%setup -q -n rpm-%{version}



%build
autoreconf -fi
%configure \
 --sysconfdir=%{_sysconfdir} \
 --localstatedir=%{_localstatedir} \
 --with-external-db \
 --with-acl \
 --program-prefix= \
 --enable-nls \
 --without-lua \
 --enable-python \
 --without-selinux \
 --libdir=/usr/lib64 \
 CPPFLAGS="-I/usr/include/nss3"

make %{?_smp_mflags}

%install
%make_install



%files
%exclude /

%files lib
/usr/lib64/librpmio.so.*

%files bin
/usr/lib/rpm/debugedit
