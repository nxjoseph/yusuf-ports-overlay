PORTNAME=	videomass
DISTVERSION=	5.0.21
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	GUI for FFmpeg and yt-dlp
WWW=		https://github.com/jeanslack/Videomass \
		https://pypi.org/project/videomass

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}PyPubSub>=4.0.3:devel/py-PyPubSub@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=2.31.0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wxPython42>=4.0.7:x11-toolkits/py-wxPython4@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}yt-dlp>0:www/py-yt-dlp@${PY_FLAVOR} \
		ffmpeg:multimedia/ffmpeg \
		yt-dlp:www/yt-dlp

USES=		python:3.8+ shebangfix
USE_PYTHON=	flavors

SHEBANG_FILES=	${WRKSRC}/launcher

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/launcher \
		${STAGEDIR}${PREFIX}/bin/videomass
	${INSTALL_DATA} ${WRKSRC}/xdg/io.github.jeanslack.videomass.desktop \
		${STAGEDIR}${DESKTOPDIR}/io.github.jeanslack.videomass.desktop
	${INSTALL_DATA} ${WRKSRC}/${PORTNAME}/data/icons/videomass.png \
		${STAGEDIR}${PREFIX}/share/pixmaps/videomass.png
	(cd ${WRKSRC}/${PORTNAME} && \
		${FIND} . -type d -exec ${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\; && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/${PORTNAME}/{} \
		\;)

.include <bsd.port.mk>
