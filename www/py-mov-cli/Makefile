PORTNAME=	mov-cli
DISTVERSION=	4.4.13
CATEGORIES=	www python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Watch everything from your terminal
WWW=		https://github.com/mov-cli/mov-cli

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}beautifulsoup>=0:www/py-beautifulsoup@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}deprecation>=0:devel/py-deprecation@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}devgoldyutils>=0:devel/py-devgoldyutils@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}httpx>=0:www/py-httpx@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}importlib-metadata>=0:devel/py-importlib-metadata@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}mov-cli-test>=0:www/py-mov-cli-test@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}packaging>=0:devel/py-packaging@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}PyInquirer>=0:devel/py-pyinquirer@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}python-decouple>=0:devel/py-python-decouple@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}thefuzz>=0:devel/py-thefuzz@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}toml>=0:textproc/py-toml@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}typer>=0:devel/py-typer@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}unidecode>=0:converters/py-unidecode@${PY_FLAVOR} \
		chafa:graphics/chafa \
		fzf:textproc/fzf \
		mpv:multimedia/mpv

USES=		python:3.8+
USE_GITHUB=	yes
GH_ACCOUNT=	mov-cli

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	(cd ${WRKSRC}/mov_cli && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli/{} \
		\;)

.include <bsd.port.mk>
