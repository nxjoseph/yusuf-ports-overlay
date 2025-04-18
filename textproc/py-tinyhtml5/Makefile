PORTNAME=	tinyhtml5
DISTVERSION=	2.0.0
CATEGORIES=	textproc python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Tiny HTML5 parser
WWW=		https://github.com/CourtBouillon/tinyhtml5 \
		https://pypi.org/project/tinyhtml5

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}webencodings>=0.5.1:converters/py-webencodings@${PY_FLAVOR}

USES=		python:3.9+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	(cd ${WRKSRC}/${PORTNAME} && \
		${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME} && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
