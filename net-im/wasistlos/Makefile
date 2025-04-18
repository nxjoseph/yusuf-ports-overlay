PORTNAME=	wasistlos
DISTVERSIONPREFIX=	v
DISTVERSION=	1.7.0
CATEGORIES=	net-im

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Unofficial WhatsApp desktop application
WWW=		https://github.com/xeco23/WasIstLos

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PREFIX}/include/canberra.h:audio/libcanberra \
		${PREFIX}/include/libayatana-appindicator3-0.1/libayatana-appindicator/app-indicator.h:devel/libayatana-appindicator
LIB_DEPENDS=	libayatana-appindicator3.so:devel/libayatana-appindicator \
		libayatana-ido3-0.4.so:devel/ayatana-ido \
		libayatana-indicator3.so:devel/libayatana-indicator \
		libcanberra.so:audio/libcanberra \
		libdbusmenu-glib.so:devel/libdbusmenu \
		libsoup-2.4.so:devel/libsoup \
		libsoup-3.0.so:devel/libsoup3 \
		libwebkit2gtk-4.1.so:www/webkit2-gtk@41

USES=		cmake compiler:c++20-lang desktop-file-utils gettext-tools \
		gnome gstreamer pkgconfig
USE_CXXSTD=	c++20
USE_GITHUB=	yes
GH_ACCOUNT=	xeco23
GH_PROJECT=	WasIstLos
USE_GNOME=	gtkmm30 intltool
USE_GSTREAMER=	bad faac faad good libav

LDFLAGS+=	-L${PREFIX}/lib

OPTIONS_DEFINE=		HUNSPELL
OPTIONS_DEFAULT=	HUNSPELL

HUNSPELL_LIB_DEPENDS=	libhunspell-1.7.so:textproc/hunspell

.include <bsd.port.mk>
