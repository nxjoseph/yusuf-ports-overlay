PORTNAME=	xclicker
DISTVERSIONPREFIX=	v
DISTVERSION=	1.5.1
CATEGORIES=	x11

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Fast gui autoclicker for x11 desktops
WWW=		https://github.com/robiot/xclicker

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		meson pkgconfig motif xorg gnome
USE_GITHUB=	yes
GH_ACCOUNT=	robiot

USE_GNOME+=	gtk30 gdkpixbuf2 glib20
USE_XORG+=	x11 xi xtst

PLIST_FILES=	bin/xclicker

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/_build/src/xclicker \
	${STAGEDIR}${PREFIX}/bin

.include <bsd.port.mk>
