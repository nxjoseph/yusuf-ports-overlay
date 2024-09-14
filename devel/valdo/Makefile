PORTNAME=	valdo
DISTVERSION=	2022.04.14
CATEGORIES=	devel

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Create new Vala projects from templates
WWW=		https://github.com/vala-lang/valdo

LICENSE=	LGPL21+
LICENSE_FILE=	${WRKSRC}/COPYING

LIB_DEPENDS=	libjson-glib-1.0.so:devel/json-glib

USES=		gnome meson pkgconfig python:build shebangfix vala:build
USE_GITHUB=	yes
GH_ACCOUNT=	vala-lang
USE_GNOME=	glib20

SHEBANG_FILES=	templates/gnome/build-aux/meson/postinstall.py

.include <bsd.port.mk>
