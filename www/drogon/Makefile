PORTNAME=	drogon
DISTVERSIONPREFIX=	v
DISTVERSION=	1.9.8
CATEGORIES=	www

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	HTTP web application framework
WWW=		https://github.com/drogonframework/drogon

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	brotli:archivers/brotli \
		doxygen:devel/doxygen
LIB_DEPENDS=	libbrotlicommon.so:archivers/brotli \
		libbrotlidec.so:archivers/brotli \
		libhiredis.so:databases/hiredis \
		libjsoncpp.so:devel/jsoncpp \
		libyaml-cpp.so:devel/yaml-cpp

USES=		cmake localbase:ldflags ssl
USE_GITHUB=	yes
GH_ACCOUNT=	drogonframework
GH_TUPLE=	an-tao:trantor:8bf280ba:trantor/trantor

OPTIONS_DEFAULT=	PGSQL

OPTIONS_SINGLE=		BACKEND
OPTIONS_SINGLE_BACKEND=	PGSQL SQLITE3

PGSQL_DESC=	Use PostgreSQL as backend
SQLITE3_DESC=	Use SQLite3 as backend

.include <bsd.port.mk>
.include <bsd.port.options.mk>

.if empty(PORT_OPTIONS:MSQLITE3) && !empty(PORT_OPTIONS:MPGSQL)
USES+=		pgsql
LIB_DEPENDS+=	libpq.so:databases/postgresql16-client
.endif
.if empty(PORT_OPTIONS:MPGSQL) && !empty(PORT_OPTIONS:MSQLITE3)
USES+=		sqlite
LIB_DEPENDS+=	libsqlite3.so:databases/sqlite3
.endif
