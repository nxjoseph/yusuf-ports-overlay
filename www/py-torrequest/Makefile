PORTNAME=	torrequest
DISTVERSION=	0.1.0
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Simple interface for HTTP requests over Tor
WWW=		https://github.com/erdiaker/torrequest \
		https://pypi.org/project/torrequest

LICENSE=	MIT

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pysocks>=1.5.7:net/py-pysocks@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=2.11.0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}stem>=1.4.0:security/py-stem@${PY_FLAVOR} \
		tor:security/tor

USES=		python:3.8+
USE_PYTHON=	autoplist distutils flavors

NO_ARCH=	yes
NO_BUILD=	yes

.include <bsd.port.mk>
