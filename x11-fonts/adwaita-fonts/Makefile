PORTNAME=	adwaita-fonts
DISTVERSION=	48.2
CATEGORIES=	x11-fonts gnome
MASTER_SITES=	GNOME/sources/${PORTNAME}/${PORTVERSION:C/^([0-9]+)\..*/\1/}
DIST_SUBDIR=	gnome

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Typefaces for GNOME
WWW=		https://gitlab.gnome.org/GNOME/adwaita-fonts

LICENSE=	GPLv3+
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		fonts meson tar:xz

FONTSDIR=	share/fonts/Adwaita
NO_ARCH=	yes

.include <bsd.port.mk>
