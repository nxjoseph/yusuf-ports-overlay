PORTNAME=	durationpy
DISTVERSION=	0.9
CATEGORIES=	converters python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Module to convert between datetime.timedelta and time.Duration strings
WWW=		https://github.com/icholy/durationpy \
		https://pypi.org/project/durationpy

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}webencodings>=0.5.1:converters/py-webencodings@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist distutils flavors

NO_ARCH=	yes

.include <bsd.port.mk>
