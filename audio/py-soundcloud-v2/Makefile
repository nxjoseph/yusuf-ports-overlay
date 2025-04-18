PORTNAME=	soundcloud-v2
DISTVERSION=	1.6.0
CATEGORIES=	audio python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Python wrapper for v2 SoundCloud API
WWW=		https://pypi.org/project/soundcloud-v2 \
		https://github.com/7x11x13/soundcloud.py

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}wheel>=0:devel/py-wheel@${PY_FLAVOR}

USES=		python:3.7+
USE_PYTHON=	autoplist distutils flavors

NO_ARCH=	yes

.include <bsd.port.mk>
