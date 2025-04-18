PORTNAME=	ytmdl
DISTVERSION=	2024.08.15.1
CATEGORIES=	www python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Simple app to get songs from YouTube in mp3 format with all metadata
WWW=		https://github.com/deepjyoti30/ytmdl \
		https://pypi.org/project/ytmdl

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}beautifulsoup>=0:www/py-beautifulsoup@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}colorama>=0:devel/py-colorama@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}downloader-cli>=0.3.4:www/py-downloader-cli@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}ffmpeg-python>=0:multimedia/py-ffmpeg-python@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}itunespy>=0:www/py-itunespy@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}musicbrainzngs>=0:www/py-musicbrainzngs@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}mutagen>=0:audio/py-mutagen@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pyDes>=0:www/py-pydes@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pysocks>=0:net/py-pysocks@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}rich>=0:textproc/py-rich@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}simber>=0.2.6:www/py-simber@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}spotipy>=0:audio/py-spotipy@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}unidecode>=0:converters/py-unidecode@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}urllib3>=0:net/py-urllib3@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}xdg>=0:devel/py-xdg@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}youtube-search-python>=0:www/py-youtube-search-python@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}yt-dlp>=2024.4.9:www/py-yt-dlp@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}ytmusicapi>=0:www/py-ytmusicapi@${PY_FLAVOR} \
		ffmpeg:multimedia/ffmpeg

USES=		python:3.6+
USE_GITHUB=	yes
GH_ACCOUNT=	deepjyoti30
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

SUB_FILES=	ytmdl
SUB_LIST=	PYTHON_CMD=${PYTHON_CMD}

do-install:
	${INSTALL_SCRIPT} ${WRKDIR}/ytmdl \
		${STAGEDIR}${PREFIX}/bin/ytmdl
	(cd ${WRKSRC}/ytmdl && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
