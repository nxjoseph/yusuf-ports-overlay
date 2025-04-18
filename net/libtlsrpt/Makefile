PORTNAME=	libtlsrpt
DISTVERSIONPREFIX=	v
DISTVERSION=	0.5.0
CATEGORIES=	net

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	C Library to implement TLSRPT into a MTA
WWW=		https://github.com/sys4/libtlsrpt

LICENSE=	LGPL3
LICENSE_FILE=	${WRKSRC}/COPYING

USES=		autoreconf gettext-tools libtool
USE_GITHUB=	yes
GH_ACCOUNT=	sys4
USE_LDCONFIG=	yes

GNU_CONFIGURE=	yes

INSTALL_TARGET=	install-strip

.include <bsd.port.mk>
