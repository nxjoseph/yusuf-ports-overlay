PORTNAME=	atunes
PORTVERSION=	3.1.2
PORTREVISION=	6
CATEGORIES=	audio java
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}/aTunes%20${PORTVERSION}
DISTNAME=	${PORTNAME}-${PORTVERSION}-bin

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Full-featured audio player and manager developed in Java
WWW=		https://sourceforge.net/projects/atunes \
		https://www.atunes.org

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/license.txt

USES=		java:run
JAVA_VERSION=	8

DESKTOP_ENTRIES=	"aTunes" \
			"Audio player and manager" \
			"${PREFIX}/share/pixmaps/atunes.png" \
			"atunes" \
			"Audio;AudioVideo;Java;" \
			true

NO_ARCH=	yes
NO_BUILD=	yes
PORTSCOUT=	skipv:3.2.0
SUB_FILES=	atunes
SUB_LIST=	DATADIR="${DATADIR}" \
		JAVA="${JAVA}"
WRKSRC=		${WRKDIR}/${PORTNAME}-${PORTVERSION}

OPTIONS_DEFINE=		CDDA2WAV
OPTIONS_DEFAULT=	CDDA2WAV LAME MPLAYER VORBIS

OPTIONS_MULTI=		ENCODER ENGINE
OPTIONS_MULTI_ENCODER=	FLAC LAME VORBIS
OPTIONS_MULTI_ENGINE=	MPLAYER XINE

CDDA2WAV_RUN_DEPENDS=	cdda2wav:sysutils/cdrtools
FLAC_RUN_DEPENDS=	flac:audio/flac
LAME_RUN_DEPENDS=	lame:audio/lame
MPLAYER_RUN_DEPENDS=	mplayer:multimedia/mplayer
VORBIS_RUN_DEPENDS=	ogg123:audio/vorbis-tools
XINE_LIB_DEPENDS=	libxine.so:multimedia/libxine

INSTALL_FILES=	aTunes.ico aTunes.jar splash.gif changelog.txt

do-install:
	@${MKDIR} ${STAGEDIR}${DATADIR}/lib
	${INSTALL_SCRIPT} ${WRKDIR}/atunes \
		${STAGEDIR}${PREFIX}/bin
.for f in ${INSTALL_FILES}
	${INSTALL_DATA} ${WRKSRC}/${f} \
		${STAGEDIR}${DATADIR}/${f}
.endfor
	@(cd ${WRKSRC} && \
		${FIND} lib -type f -name "*.jar" -exec ${INSTALL_DATA} {} \
		${STAGEDIR}${DATADIR}/{} \;)
	@(cd ${WRKSRC} && \
		${COPYTREE_SHARE} settings ${STAGEDIR}${DATADIR}/)
	${INSTALL_DATA} ${WRKSRC}/atunes.png \
		${STAGEDIR}${PREFIX}/share/pixmaps

.include <bsd.port.mk>
