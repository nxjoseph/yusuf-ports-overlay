PORTNAME=	varia
DISTVERSIONPREFIX=	v
DISTVERSION=	2025.1.24
CATEGORIES=	www python

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Download manager based on aria2
WWW=		https://github.com/giantpinkrobots/varia

LICENSE=	MPL20
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	aria2c:www/aria2 \
		aria2p:www/py-aria2p@${PY_FLAVOR} \
		ffmpeg:multimedia/ffmpeg \
		yt-dlp-devel:www/py-yt-dlp@${PY_FLAVOR}

USES=		gettext-tools gnome meson python shared-mime-info shebangfix
USE_GITHUB=	yes
GH_ACCOUNT=	giantpinkrobots
USE_GNOME=	glib20 gtk40 libadwaita
GLIB_SCHEMAS=	io.github.giantpinkrobots.varia.gschema.xml

SHEBANG_FILES=	src/varia.in
BINARY_ALIAS=	python3=${PYTHON_CMD}

post-patch:
	@${REINPLACE_CMD} -e '/update_desktop_database/d' \
		${WRKSRC}/meson.build
	@${REINPLACE_CMD} -e '1s|.*|#!${PYTHON_CMD}|' \
		${WRKSRC}/src/varia-py.in
	@${REINPLACE_CMD} -E \
		-e '2s|.*|pythonexec="${PYTHON_CMD}"|' \
		-e '3s|.*|pkgdatadir="${DATADIR}"|' \
		-e '5s|.*|aria2cexec="${PREFIX}/bin/aria2c"|' \
		-e '6s|.*|ffmpegexec="${PREFIX}/bin/ffmpeg"|' \
		-e '20,21d; 23,25d;' \
		${WRKSRC}/src/varia.in

.include <bsd.port.mk>
