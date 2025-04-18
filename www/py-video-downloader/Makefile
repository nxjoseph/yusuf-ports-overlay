PORTNAME=	video-downloader
DISTVERSIONPREFIX=	v
DISTVERSION=	0.12.22
CATEGORIES=	www python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Download videos from websites like YouTube and many others
WWW=		https://github.com/Unrud/video-downloader

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/COPYING

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}xattr>=0.8.1:devel/py-xattr@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}yt-dlp>=2024.12.23:www/py-yt-dlp@${PY_FLAVOR}

USES=		gettext-tools gnome meson python:3.8+
USE_GITHUB=	yes
GH_ACCOUNT=	Unrud
USE_GNOME=	gtk-update-icon-cache librsvg2

NO_ARCH=	yes

post-patch:
	@${REINPLACE_CMD} -e 's|python3|python${PYTHON_VER}|g' \
		-e '/update_desktop_database/d' \
		-e '/gtk_update_icon_cache/d' \
		${WRKSRC}/meson.build

.include <bsd.port.mk>
