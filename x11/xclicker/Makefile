PORTNAME=	xclicker
DISTVERSIONPREFIX=	v
DISTVERSION=	1.5.1
CATEGORIES=	x11

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Fast gui autoclicker for x11 desktops
WWW=		https://github.com/robiot/xclicker

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		meson pkgconfig motif xorg gnome desktop-file-utils
USE_GITHUB=	yes
GH_ACCOUNT=	robiot
USE_GNOME+=	gtk30 gdkpixbuf2 glib20
USE_XORG+=	x11 xi xtst

PLIST_FILES=	bin/xclicker \
		share/applications/xclicker.desktop \
		share/pixmaps/xclicker.png

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/_build/src/${PORTNAME} \
	${STAGEDIR}${PREFIX}/bin
	${INSTALL_DATA} ${PATCHDIR}/${PORTNAME}.desktop \
		${STAGEDIR}${DESKTOPDIR}/${PORTNAME}.desktop
	${INSTALL_DATA} ${WRKSRC}/assets/icon.png \
		${STAGEDIR}${PREFIX}/share/pixmaps/${PORTNAME}.png

.include <bsd.port.mk>
