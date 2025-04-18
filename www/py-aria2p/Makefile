PORTNAME=	aria2p
DISTVERSION=	0.12.1
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Command-line tool and library to interact with an aria2c daemon
WWW=		https://github.com/pawamoy/aria2p \
		https://pypi.org/project/aria2p

LICENSE=	ISCL
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}loguru>=0.5:devel/py-loguru@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}platformdirs>=4.2:devel/py-platformdirs@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=2.19:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}tomli>=2.0:textproc/py-tomli@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}websocket-client>=0.58:www/py-websocket-client@${PY_FLAVOR}

USES=		python:3.9+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

SUB_FILES=	${PORTNAME}
SUB_LIST=	PYTHON_CMD=${PYTHON_CMD}

OPTIONS_DEFINE=	TUI

TUI_DESC=		Enable interactive interface
TUI_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}asciimatics>=1.13:devel/py-asciimatics@${PY_FLAVOR} \
			${PYTHON_PKGNAMEPREFIX}pyperclip>=0:devel/py-pyperclip@${PY_FLAVOR}

do-install:
	${INSTALL_SCRIPT} ${WRKDIR}/${PORTNAME} \
		${STAGEDIR}${PREFIX}/bin/${PORTNAME}
	(cd ${WRKSRC}/src/${PORTNAME} && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
