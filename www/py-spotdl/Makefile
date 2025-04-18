PORTNAME=	spotdl
DISTVERSION=	4.2.11
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Download your Spotify playlists and songs
WWW=		https://github.com/spotDL/spotify-downloader

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}beautifulsoup>=4.12.3:www/py-beautifulsoup@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}fastapi>=0.103.0:www/py-fastapi@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}mutagen>=1.47.0:audio/py-mutagen@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}platformdirs>=4.3.6:devel/py-platformdirs@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pydantic2>=2.9.2:devel/py-pydantic2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pykakasi>=2.3.0:japanese/py-pykakasi@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}python-dateutil>=0:devel/py-python-dateutil@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}python-slugify>=8.0.4:textproc/py-python-slugify@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pytube>=15.0.0:multimedia/py-pytube@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}rapidfuzz>=3.10.1:devel/py-rapidfuzz@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=2.32.3:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}rich>=13.9.4:textproc/py-rich@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}soundcloud-v2>=1.6.0:audio/py-soundcloud-v2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}spotipy>=2.24.0:audio/py-spotipy@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}syncedlyrics>=1.0.1:multimedia/py-syncedlyrics@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}unidecode>=0:converters/py-unidecode@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}uvicorn>=0.23.2:www/py-uvicorn@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}websockets>=14.1:devel/py-websockets@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}yt-dlp>=2025.1.15:www/py-yt-dlp@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}ytmusicapi>=0:www/py-ytmusicapi@${PY_FLAVOR} \
		ffmpeg:multimedia/ffmpeg

USES=		python:3.9+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

post-patch:
	@${REINPLACE_CMD} '1s|^|#!${PYTHON_CMD}\n|' \
		${WRKSRC}/${PORTNAME}/__main__.py
	@${RM} ${WRKSRC}/${PORTNAME}/__main__.py.bak

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/${PORTNAME}/__main__.py \
		${STAGEDIR}${PREFIX}/bin/${PORTNAME}
	(cd ${WRKSRC}/${PORTNAME} && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
