PORTNAME=	soundcloud-v2
DISTVERSIONPREFIX=	v
DISTVERSION=	1.6.0
CATEGORIES=	audio python
#MASTER_SITES=	https://codeberg.org/miurahr/pykakasi/archive/${DISTVERSIONFULL}${EXTRACT_SUFX}?dummy=/
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Python wrapper for v2 SoundCloud API
WWW=		https://github.com/7x11x13/soundcloud.py

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools>=0:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>=0:devel/py-wheel@${PY_FLAVOR}

USES=		python:3.7+
USE_PYTHON=	autoplist distutils flavors
USE_GITHUB=	yes
GH_ACCOUNT=	7x11x13
GH_PROJECT=	soundcloud.py

NO_ARCH=	yes

.include <bsd.port.mk>
