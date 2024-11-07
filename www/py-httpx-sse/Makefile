PORTNAME=	httpx-sse
DISTVERSION=	0.4.0
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Consume Server-Sent Event (SSE) messages with HTTPX
WWW=		https://github.com/florimondmanca/httpx-sse

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}black>=23.12.0:devel/py-black@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}httpx>=0.26.0:www/py-httpx@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}mypy>=1.8.0:devel/py-mypy@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pytest>=7.4.3:devel/py-pytest@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pytest-asyncio>=0.21.1:devel/py-pytest-asyncio@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pytest-cov>=0:devel/py-pytest-cov@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}ruff>=0.1.9:devel/py-ruff@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}sse-starlette>=1.8.2:www/py-sse-starlette@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}starlette>=0.27.0:www/py-starlette@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}twine>=0:devel/py-twine@${PY_FLAVOR}

USES=		python:3.8+
USE_PYTHON=	autoplist distutils flavors

NO_ARCH=	yes

.include <bsd.port.mk>
