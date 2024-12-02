PORTNAME=	sherlock
DISTVERSION=	0.15.0
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=	sherlock_project-${DISTVERSION}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Hunt down social media accounts by username across social networks
WWW=		https://github.com/sherlock-project/sherlock \
		https://pypi.org/project/sherlock-project

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}certifi>=2019.6.16:security/py-certifi@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}colorama>=0.4.1:devel/py-colorama@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}openpyxl>=3.0.10:textproc/py-openpyxl@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pandas>=2.2.1:math/py-pandas@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pysocks>=1.7.0:net/py-pysocks@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests-futures>=1.0.0:www/py-requests-futures@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=2.22.0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}stem>=1.8.0:security/py-stem@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}torrequest>=0.1.0:www/py-torrequest@${PY_FLAVOR}

USES=		python:3.9+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

post-patch:
	${REINPLACE_CMD} '1d' \
		${WRKSRC}/sherlock_project/__main__.py
	${REINPLACE_CMD} '1s|^|#!${PYTHON_CMD}\n|' \
		${WRKSRC}/sherlock_project/__main__.py
	${RM} ${WRKSRC}/sherlock_project/__main__.py.bak

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/sherlock_project/__main__.py \
		${STAGEDIR}${PREFIX}/bin/${PORTNAME}
	(cd ${WRKSRC}/sherlock_project && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/sherlock_project/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/sherlock_project/{} \
		\;)

.include <bsd.port.mk>
