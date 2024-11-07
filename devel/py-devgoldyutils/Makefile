PORTNAME=	devgoldyutils
PORTVERSION=	3.0.0
CATEGORIES=	devel python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Goldy's small python utils library
WWW=		https://github.com/THEGOLDENPRO/devgoldyutils

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		python:3.7+
USE_GITHUB=	yes
GH_ACCOUNT=	THEGOLDENPRO
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}
	${INSTALL_DATA} ${WRKSRC}/${PORTNAME}/* ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/

.include <bsd.port.mk>
