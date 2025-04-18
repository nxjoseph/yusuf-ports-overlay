PORTNAME=	itunespy
DISTVERSION=	1.6.1
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Simple library to fetch data from the iTunes Store API
WWW=		http://github.com/sleepyfran/itunespy \
		https://pypi.org/project/itunespy

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}country>=19.8:devel/py-country@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=2.8:www/py-requests@${PY_FLAVOR}

USES=		python:3.5+
USE_PYTHON=	autoplist distutils flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

.include <bsd.port.mk>
