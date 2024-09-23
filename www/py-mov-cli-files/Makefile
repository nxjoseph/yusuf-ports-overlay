PORTNAME=	mov-cli-files
DISTVERSION=	1.1.1
CATEGORIES=	www python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Mov-cli v4 plugin for playing Music or Videos stored on your device
WWW=		https://github.com/mov-cli/mov-cli-files

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}thefuzz>=0:devel/py-thefuzz@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}mov-cli>=4.3.14:www/py-mov-cli@${PY_FLAVOR}

USES=		python:3.8+
USE_GITHUB=	yes
GH_ACCOUNT=	mov-cli

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	(cd ${WRKSRC}/mov_cli_files && \
		${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli_files/ && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli_files/{} \
		\;)

.include <bsd.port.mk>
