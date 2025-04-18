PORTNAME=	simber
DISTVERSION=	0.2.6
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Simple, minimal, powerful logging library for Python
WWW=		https://github.com/deepjyoti30/simber \
		https://pypi.org/project/simber

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}colorama>=0:devel/py-colorama@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist distutils flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

.include <bsd.port.mk>
