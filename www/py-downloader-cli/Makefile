PORTNAME=	downloader
DISTVERSION=	0.3.4
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
PKGNAMESUFFIX=	-cli
DISTNAME=	downloader_cli-${DISTVERSION}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Simple downloader with an awesome progressbar
WWW=		https://github.com/deepjyoti30/downloader-cli \
		https://pypi.org/project/downloader-cli

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}urllib3>=1.25.6:net/py-urllib3@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist distutils flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

.include <bsd.port.mk>
