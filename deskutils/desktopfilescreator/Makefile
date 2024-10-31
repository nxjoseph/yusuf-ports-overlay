PORTNAME=	desktopfilescreator
DISTVERSION=	1.2.7
CATEGORIES=	deskutils

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Simple app for creating .desktop files
WWW=		https://github.com/alexkdeveloper/desktop-files-creator

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/COPYING

LIB_DEPENDS=	libadwaita-1.so:x11-toolkits/libadwaita \
		libgtk-4.so:x11-toolkits/gtk40

USES=		gettext-runtime gnome meson pkgconfig vala:build
USE_GITHUB=	yes
GH_ACCOUNT=	alexkdeveloper
GH_PROJECT=	desktop-files-creator
USE_GNOME=	glib20

OPTIONS_DEFINE=	NLS
OPTIONS_SUB=	yes
NLS_USES=	gettext

post-patch:
	@${REINPLACE_CMD} -e '/update_desktop_database/d' \
		${WRKSRC}/meson.build

.include <bsd.port.mk>
