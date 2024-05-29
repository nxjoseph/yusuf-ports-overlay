PORTNAME=	ytDownloader
DISTVERSIONPREFIX=	v
DISTVERSION=	3.17.4
CATEGORIES=	www

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	GUI video downloader supporting hundreds of sites
WWW=		https://github.com/aandrew-me/ytDownloader

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	npm:www/npm-node20
RUN_DEPENDS=	electron27:devel/electron27 \
		ffmpeg:multimedia/ffmpeg \
		yt-dlp:www/yt-dlp

USES=		nodejs desktop-file-utils
USE_GITHUB=	yes
GH_ACCOUNT=	aandrew-me

NO_BUILD=	yes

post-patch:
	${CP} ${PATCHDIR}/ytdownloader ${WRKSRC}
	${CP} ${PATCHDIR}/ytdownloader.desktop ${WRKSRC}

pre-install:
	${RM} ${WRKSRC}/windows.sh ${WRKSRC}/linux.sh
	${RM} -rf ${WRKSRC}/flatpak
	cd ${WRKSRC} && npm i
	${RM} ${WRKSRC}/package-lock.json

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/ytdownloader ${STAGEDIR}${PREFIX}/bin
	${INSTALL_DATA} ${WRKSRC}/ytdownloader.desktop ${STAGEDIR}${PREFIX}/share/applications
	${CP} -r ${WRKSRC} ${STAGEDIR}${PREFIX}/share/${PORTNAME}
	${INSTALL_DATA} ${WRKSRC}/resources/icon.png \
		${STAGEDIR}${PREFIX}/share/icons/${PORTNAME}.png

post-install:
	${LN} -sf ${PREFIX}/bin/python${PYTHON_DEFAULT} ${LOCALBASE}/bin/python3
	${LN} -sf ${PREFIX}/bin/electron27 ${LOCALBASE}/bin/electron

post-stage:
	${RM} ${STAGEDIR}${PREFIX}/share/ytDownloader/node_modules/jake/bin/bash_completion.sh

.include <bsd.port.mk>
