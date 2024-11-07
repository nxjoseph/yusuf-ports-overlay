PORTNAME=	movcli
DISTVERSION=	1.1.7
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
PKGNAMESUFFIX=	-test
DISTNAME=	mov_cli_test-${DISTVERSION}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Mov-cli v4 plugin to test mov-cli's capabilities
WWW=		https://github.com/mov-cli/mov-cli-test

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pytubefix>=0:multimedia/py-pytubefix@${PY_FLAVOR}

USES=		python:3.8+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	(cd ${WRKSRC}/mov_cli_test && \
		${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli_test/ && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli_test/{} \
		\;)

.include <bsd.port.mk>
