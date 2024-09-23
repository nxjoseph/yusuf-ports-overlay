PORTNAME=	mov-cli-jellyplex
DISTVERSION=	1.1.2
CATEGORIES=	www python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Mov-cli v4 plugin for watching content from jellyfin or plex
WWW=		https://github.com/mov-cli/mov-cli-jellyplex

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}requests>=0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}importlib-metadata>=0:devel/py-importlib-metadata@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}plexapi>=0:multimedia/py-plexapi@${PY_FLAVOR}

USES=		python:3.8+
USE_GITHUB=	yes
GH_ACCOUNT=	mov-cli

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	(cd ${WRKSRC}/mov_cli_jellyplex && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli_jellyplex/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli_jellyplex/{} \
		\;)

.include <bsd.port.mk>
