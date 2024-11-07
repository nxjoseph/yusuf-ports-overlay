PORTNAME=	pykakasi
DISTVERSION=	2.3.0
CATEGORIES=	japanese python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Lightweight converter from Japanese Kana-kanji sentences to Kana-Roman
WWW=		https://codeberg.org/miurahr/pykakasi

LICENSE=	GPLv3+
LICENSE_FILE=	${WRKSRC}/COPYING

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools-scm>=3.5.0:devel/py-setuptools-scm@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}setuptools>=42:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>=0:devel/py-wheel@${PY_FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}deprecated>=0:devel/py-deprecated@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}importlib-resources>=0:devel/py-importlib-resources@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}jaconv>=0:japanese/py-jaconv@${PY_FLAVOR}

USES=		python:3.8+
USE_PYTHON=	autoplist distutils flavors

NO_ARCH=	yes

post-install:
	(cd ${WRKSRC}/build/lib/${PORTNAME}/data && \
		${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/data && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/data/{} \
		\;) && \
		(cd ${WRKSRC}/src && \
		${INSTALL_DATA} kakasidict.py \
		${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/)

.include <bsd.port.mk>
