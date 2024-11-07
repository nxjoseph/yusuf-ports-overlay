PORTNAME=	spotdl
DISTVERSIONPREFIX=	v
DISTVERSION=	4.2.8
CATEGORIES=	www python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Download your Spotify playlists and songs
WWW=		https://github.com/spotDL/spotify-downloader

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}beautifulsoup>=0:www/py-beautifulsoup@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}fastapi>=0:www/py-fastapi@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}mutagen>=0:audio/py-mutagen@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}platformdirs>=0:devel/py-platformdirs@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pydantic2>=0:devel/py-pydantic2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pykakasi>=0:japanese/py-pykakasi@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}python-slugify>=0:textproc/py-python-slugify@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pytube>=0:multimedia/py-pytube@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}rapidfuzz>=0:devel/py-rapidfuzz@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}rich>=0:textproc/py-rich@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}soundcloud-v2>=0:audio/py-soundcloud-v2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}spotipy>=0:audio/py-spotipy@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}syncedlyrics>=0:multimedia/py-syncedlyrics@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}unidecode>=0:converters/py-unidecode@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}uvicorn>=0:www/py-uvicorn@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}yt-dlp>=0:www/py-yt-dlp@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}ytmusicapi>=0:www/py-ytmusicapi@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}python-dateutil>=0:devel/py-python-dateutil@${PY_FLAVOR} \
		ffmpeg:multimedia/ffmpeg

USES=		python:3.8+
USE_GITHUB=	yes
GH_ACCOUNT=	spotDL
GH_PROJECT=	spotify-downloader
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

post-patch:
	${REINPLACE_CMD} '1s|^|#!${PYTHON_CMD}\n|' \
		${WRKSRC}/${PORTNAME}/__main__.py
	${RM} ${WRKSRC}/${PORTNAME}/__main__.py.bak

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/${PORTNAME}/__main__.py ${STAGEDIR}${PREFIX}/bin/${PORTNAME}
	(cd ${WRKSRC}/${PORTNAME} && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
