PORTNAME=	youtube
DISTVERSION=	1.6.6
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
PKGNAMESUFFIX=	-search-python
DISTNAME=	youtube-search-python-${DISTVERSION}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Search for YouTube videos/playlists, channels & get video information
WWW=		https://github.com/alexmercerind/youtube-search-python \
		https://pypi.org/project/youtube-search-python

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}httpx>=0.14.2:www/py-httpx@${PY_FLAVOR}

USES=		python:3.6+
USE_PYTHON=	autoplist distutils flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

.include <bsd.port.mk>
