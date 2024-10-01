PORTNAME=	video-downloader
DISTVERSIONPREFIX=	v
DISTVERSION=	0.12.18
CATEGORIES=	www python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Download videos from websites like YouTube and many others
WWW=		https://github.com/Unrud/video-downloader

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/COPYING

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}xattr>=0:devel/py-xattr@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}yt-dlp>=0:www/py-yt-dlp@${PY_FLAVOR}

USES=		gettext gnome meson python:3.8+
USE_GITHUB=	yes
GH_ACCOUNT=	Unrud

NO_ARCH=	yes

pre-configure:
	@${REINPLACE_CMD} -e 's|python3|python${PYTHON_VER}|g' \
		${WRKSRC}/meson.build

.include <bsd.port.mk>
