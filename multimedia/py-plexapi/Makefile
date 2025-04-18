PORTNAME=	plexapi
DISTVERSION=	4.16.1
CATEGORIES=	multimedia python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Python bindings for the Plex API
WWW=		https://github.com/pkkid/python-plexapi

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE.txt

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}requests>=0:www/py-requests@${PY_FLAVOR}

USES=		python:3.9+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes

do-install:
	(cd ${WRKSRC}/${PORTNAME} && \
		${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME} && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
