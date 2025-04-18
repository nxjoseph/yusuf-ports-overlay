PORTNAME=	syncedlyrics
DISTVERSION=	1.0.1
CATEGORIES=	multimedia python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Get an LRC format (synchronized) lyrics for your music
WWW=		https://pypi.org/project/syncedlyrics \
		https://github.com/moehmeni/syncedlyrics

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}beautifulsoup>=4.12.3:www/py-beautifulsoup@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}rapidfuzz>=3.6.2:devel/py-rapidfuzz@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=2.31.0:www/py-requests@${PY_FLAVOR}

USES=		python:3.8+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

post-patch:
	@${REINPLACE_CMD} '1s|^|#!${PYTHON_CMD}\n|' \
		${WRKSRC}/${PORTNAME}/__main__.py
	@${RM} ${WRKSRC}/${PORTNAME}/__main__.py.bak

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/${PORTNAME}/__main__.py \
		${STAGEDIR}${PREFIX}/bin/${PORTNAME}
	@(cd ${WRKSRC}/${PORTNAME} && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
