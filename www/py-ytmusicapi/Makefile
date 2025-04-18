PORTNAME=	ytmusicapi
DISTVERSION=	1.10.1
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Unofficial API for YouTube Music
WWW=		https://pypi.org/project/ytmusicapi \
		https://github.com/sigma67/ytmusicapi

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}requests>=2.22:www/py-requests@${PY_FLAVOR}

USES=		gettext-tools python:3.9+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	(cd ${WRKSRC}/${PORTNAME} && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
