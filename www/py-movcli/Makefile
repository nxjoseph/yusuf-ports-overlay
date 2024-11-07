PORTNAME=	movcli
DISTVERSION=	4.4.15
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=	mov_cli-${DISTVERSION}

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
		${PYTHON_PKGNAMEPREFIX}inquirer>=0:devel/py-inquirer@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}packaging>=0:devel/py-packaging@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}python-decouple>=0:devel/py-python-decouple@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}thefuzz>=0:devel/py-thefuzz@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}toml>=0:textproc/py-toml@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}typer>=0:devel/py-typer@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}unidecode>=0:converters/py-unidecode@${PY_FLAVOR} \
		chafa:graphics/chafa \
		fzf:textproc/fzf

USES=		python:3.8+
USE_PYTHON=	flavors

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

SUB_FILES=	mov-cli mov-cli-dev
SUB_LIST=	PYTHON_CMD=${PYTHON_CMD}

OPTIONS_DEFINE=		FILES JELLYPLEX MPV SOUNDCLOUD SYNCPLAY TEST VLC \
			YOUTUBE
OPTIONS_DEFAULT=	FILES JELLYPLEX MPV SOUNDCLOUD TEST YOUTUBE
FILES_DESC=		Install plugin for playing audios and videos stored locally
JELLYPLEX_DESC=		Install plugin for streaming content from Jellyplex or Plex
MPV_DESC=		Use mpv video player in order to play content
SOUNDCLOUD_DESC=	Install plugin for playing SoundCloud
SYNCPLAY_DESC=		Use syncplay video player in order to play content
TEST_DESC=		Install plugin to test capabilities of movcli
VLC_DESC=		Use vlc video player in order to play content
YOUTUBE_DESC=		Install plugin for watching YouTube

FILES_RUN_DEPENDS=	${PYTHON_SITELIBDIR}/mov_cli_files/__init__.py:www/py-movcli-files@${PY_FLAVOR}
JELLYPLEX_RUN_DEPENDS=	${PYTHON_SITELIBDIR}/mov_cli_jellyplex/__init__.py:www/py-movcli-jellyplex@${PY_FLAVOR}
MPV_RUN_DEPENDS=	mpv:multimedia/mpv
SOUNDCLOUD_RUN_DEPENDS=	${PYTHON_SITELIBDIR}/mov_cli_soundcloud/__init__.py:www/py-movcli-soundcloud@${PY_FLAVOR}
SYNCPLAY_RUN_DEPENDS=	syncplay:multimedia/syncplay
TEST_RUN_DEPENDS=	${PYTHON_SITELIBDIR}/mov_cli_test/__init__.py:www/py-movcli-test@${PY_FLAVOR}
VLC_RUN_DEPENDS=	vlc:multimedia/vlc
YOUTUBE_RUN_DEPENDS=	${PYTHON_SITELIBDIR}/mov_cli_youtube/__init__.py:www/py-movcli-youtube@${PY_FLAVOR}

do-install:
	${INSTALL_SCRIPT} ${WRKDIR}/mov-cli \
		${STAGEDIR}${PREFIX}/bin/mov-cli
	${INSTALL_SCRIPT} ${WRKDIR}/mov-cli-dev \
		${STAGEDIR}${PREFIX}/bin/mov-cli-dev
	(cd ${WRKSRC}/mov_cli && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/mov_cli/{} \
		\;)

.include <bsd.port.mk>
