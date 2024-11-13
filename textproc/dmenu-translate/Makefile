PORTNAME=	dmenu-translate
DISTVERSIONPREFIX=	v
DISTVERSION=	1.0.0
CATEGORIES=	textproc
MASTER_SITES=	GH

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Quick text translation with dmenu
WWW=		https://github.com/NikitaIvanovV/dmenu-translate \
		https://github.com/nxjosephofficial/dmenu-translate

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	gsed:textproc/gsed \
		notify-send:devel/libnotify \
		trans:textproc/translate-shell \
		xterm:x11/xterm

USE_GITHUB=	yes
GH_ACCOUNT=	nxjosephofficial

NO_ARCH=	yes
NO_BUILD=	yes

PLIST_FILES=	${PORTEXAMPLES}${EXAMPLESDIR}/config.sh \
		bin/${PORTNAME}

OPTIONS_DEFINE=		WAYLAND X11
OPTIONS_DEFAULT=	X11
WAYLAND_DESC=		Use wmenu application and wl-clipboard clipboard manager
X11_DESC=		Use dmenu application and xclip clipboard manager

WAYLAND_RUN_DEPENDS=	wl-copy:x11/wl-clipboard \
			wmenu:x11/wmenu
X11_RUN_DEPENDS=	dmenu:x11/dmenu \
			xclip:x11/xclip

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/${PORTNAME} \
		${STAGEDIR}${PREFIX}/bin/${PORTNAME}

post-install:
	${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
	(cd ${WRKSRC}/examples && \
		${COPYTREE_SHARE} . ${STAGEDIR}${EXAMPLESDIR})

.include <bsd.port.mk>
