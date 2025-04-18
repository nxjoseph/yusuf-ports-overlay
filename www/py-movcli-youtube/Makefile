PORTNAME=	movcli
DISTVERSION=	1.3.8
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
PKGNAMESUFFIX=	-youtube
DISTNAME=	mov_cli_youtube-${DISTVERSION}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Mov-cli v4 plugin for watching youtube
WWW=		https://github.com/mov-cli/mov-cli-youtube

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}importlib-metadata>=0:devel/py-importlib-metadata@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pytubefix>=0:multimedia/py-pytubefix@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}yt-dlp>=0:www/py-yt-dlp@${PY_FLAVOR}

USES=		python:3.8+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	(cd ${WRKSRC}/mov_cli_youtube && \
		${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli_youtube/ && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli_youtube/{} \
		\;)

.include <bsd.port.mk>
