PORTNAME=	pytubefix
DISTVERSION=	8.12.3
CATEGORIES=	multimedia python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Library for downloading YouTube Videos
WWW=		https://github.com/JuanBindez/pytubefix \
		https://pypi.org/project/pytubefix

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		python:3.7+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	@(cd ${WRKSRC}/${PORTNAME} && \
		${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME} && \
		${FIND} . -type d -exec ${MKDIR} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
