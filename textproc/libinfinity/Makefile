PORTNAME=	libinfinity
PORTVERSION=	0.7.2
CATEGORIES=	textproc
MASTER_SITES=	https://github.com/gobby/libinfinity/releases/download/${DISTVERSION}/

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Collaborative editing library
WWW=		https://github.com/gobby/libinfinity

LICENSE=	LGPL21
LICENSE_FILE=	${WRKSRC}/COPYING

BUILD_DEPENDS=	gtkdocize:textproc/gtk-doc \
		intltoolize:textproc/intltool
LIB_DEPENDS=	libatk-1.0.so:accessibility/at-spi2-core \
		libavahi-client.so:net/avahi-app \
		libcairo-gobject.so:graphics/cairo \
		libcairo.so:graphics/cairo \
		libdaemon.so:devel/libdaemon \
		libgdk_pixbuf-2.0.so:graphics/gdk-pixbuf2 \
		libglib-2.0.so:devel/glib20 \
		libgnutls.so:security/gnutls \
		libgobject-2.0.so:devel/glib20 \
		libgsasl.so:security/libgsasl \
		libgtk-3.so:x11-toolkits/gtk30 \
		libharfbuzz.so:print/harfbuzz \
		libpango-1.0.so:x11-toolkits/pango \
		libpangocairo-1.0.so:x11-toolkits/pango \
		libxml2.so:textproc/libxml2

USES=		autoreconf gettext gmake gnome libtool:build pathfix pkgconfig
USE_GNOME=	cairo gdkpixbuf2 libxml2 pango
USE_LDCONFIG=	yes

GNU_CONFIGURE=	yes

INSTALL_TARGET=	install-strip

.include <bsd.port.mk>
