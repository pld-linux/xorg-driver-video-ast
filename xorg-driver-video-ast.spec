Summary:	X.org video driver for ASpeed Technologies video adapters
Summary(pl.UTF-8):	Sterownik obrazu X.org do kart graficznych ASpeed Technologies
Name:		xorg-driver-video-ast
Version:	1.1.5
Release:	5
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ast-%{version}.tar.bz2
# Source0-md5:	4f85febe48d51e53624550a96fc9e9ee
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	XFree86-driver-aspeed < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for video adapters based on ASpeed Technologies
chipsets: AST1180, AST2000, AST2100, AST2200, AST2300, AST2400,
AST2500.

%description -l pl.UTF-8
Sterownik obrazu X.org do kart graficznych opartych na układach firmy
ASpeed Technologies: AST1180, AST2000, AST2100, AST2200, AST2300,
AST2400, AST2500.

%prep
%setup -q -n xf86-video-ast-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ast_drv.so
#%{_mandir}/man4/ast.4*
