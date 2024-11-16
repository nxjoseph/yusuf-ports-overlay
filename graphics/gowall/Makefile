PORTNAME=	gowall
DISTVERSIONPREFIX=	v
DISTVERSION=	0.1.9
CATEGORIES=	graphics

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Tool to convert a Wallpaper's color scheme and palette
WWW=		https://github.com/Achno/gowall

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	xdg-open:devel/xdg-utils

USES=		go:1.22,modules

GO_MODULE=	github.com/Achno/gowall

PLIST_FILES=	bin/gowall

.include <bsd.port.mk>
