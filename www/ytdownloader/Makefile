PORTNAME=	YTDownloader
DISTVERSIONPREFIX=	v
DISTVERSION=	3.18.1_1
CATEGORIES=	www
MASTER_SITES=	https://github.com/nxjosephofficial/ytDownloader/releases/download/${DISTVERSIONPREFIX}${DISTVERSION}/:0 \
		https://raw.githubusercontent.com/aandrew-me/ytDownloader/main/:1 \
		https://raw.githubusercontent.com/aandrew-me/ytDownloader/main/resources/:2
DISTNAME=	${PORTNAME}_Linux_x86_64
DISTFILES=	${DISTNAME}${EXTRACT_SUFX}:0 \
		LICENSE:1 \
		icon.png:2
DIST_SUBDIR=	${PORTNAME}
EXTRACT_ONLY=	${DISTNAME}${EXTRACT_SUFX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	GUI video downloader supporting hundreds of sites
WWW=		https://github.com/aandrew-me/ytDownloader

LICENSE=	GPLv3

ONLY_FOR_ARCHS=	amd64
LIB_DEPENDS=	libatk-1.0.so:accessibility/at-spi2-core \
		libatk-bridge-2.0.so:accessibility/at-spi2-core \
		libatspi.so:accessibility/at-spi2-core \
		libcups.so:print/cups \
		libdav1d.so:multimedia/dav1d \
		libdbus-1.so:devel/dbus \
		libdrm.so:graphics/libdrm \
		libepoll-shim.so:devel/libepoll-shim \
		libevent.so:devel/libevent \
		libexpat.so:textproc/expat2 \
		libffi.so:devel/libffi \
		libFLAC.so:audio/flac \
		libfontconfig.so:x11-fonts/fontconfig \
		libharfbuzz-subset.so:print/harfbuzz \
		libharfbuzz.so:print/harfbuzz \
		libicudata.so:devel/icu \
		libicui18n.so:devel/icu \
		libicuuc.so:devel/icu \
		libnspr4.so:devel/nspr \
		libnss3.so:security/nss \
		libnssutil3.so:security/nss \
		libopenh264.so:multimedia/openh264 \
		libopus.so:audio/opus \
		libpci.so:devel/libpci \
		libpipewire-0.3.so:multimedia/pipewire \
		libplc4.so:devel/nspr \
		libplds4.so:devel/nspr \
		libpng16.so:graphics/png \
		libsmime3.so:security/nss \
		libsndio.so:audio/sndio \
		libwayland-client.so:graphics/wayland \
		libwebp.so:graphics/webp \
		libwebpdemux.so:graphics/webp \
		libwebpmux.so:graphics/webp \
		libxkbcommon.so:x11/libxkbcommon \
		libxshmfence.so:x11/libxshmfence
RUN_DEPENDS=	ffmpeg:multimedia/ffmpeg \
		yt-dlp:www/yt-dlp

USES=		electronfix:30 gettext-runtime jpeg zip gl gnome xorg motif
USE_GL=		egl gbm gl
USE_GNOME=	cairo gdkpixbuf2 glib20 gtk30 libxml2 libxslt pango
USE_XORG=	x11 xcb xcomposite xdamage xext xfixes xi xrandr xrender xtst

NO_BUILD=	yes
SUB_FILES=	ytdownloader

NO_WRKSUBDIR=	yes

do-install:
	cd ${WRKSRC} && \
		${COPYTREE_SHARE} \* ${STAGEDIR}${DATADIR}
	${INSTALL_SCRIPT} ${WRKDIR}/ytdownloader \
		${STAGEDIR}${PREFIX}/bin/ytdownloader
	${INSTALL_DATA} ${PATCHDIR}/ytdownloader.desktop \
		${STAGEDIR}${DESKTOPDIR}/ytdownloader.desktop
	${INSTALL_DATA} ${DISTDIR}/${PORTNAME}/icon.png \
		${STAGEDIR}${PREFIX}/share/pixmaps/YTDownloader.png

ELECTRONFIX_MAIN_EXECUTABLE=	ytdownloader
LICENSE_DISTFILES_GPLV3=	LICENSE

.include <bsd.port.mk>
