PORTNAME=	devgoldyutils
PORTVERSION=	3.0.0
CATEGORIES=	devel python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Goldy's small python utils library
WWW=		https://pypi.org/project/devgoldyutils \
		https://github.com/THEGOLDENPRO/devgoldyutils

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		python:3.7+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	@(cd ${WRKSRC}/${PORTNAME} && \
		${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME} && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
