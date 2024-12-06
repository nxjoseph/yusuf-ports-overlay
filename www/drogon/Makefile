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

OPTIONS_DEFAULT=	PGSQL16

OPTIONS_SINGLE=		BACKEND
OPTIONS_SINGLE_BACKEND=	MYSQL80 PGSQL16 SQLITE3

MYSQL80_DESC=	Use MySQL80 as backend
PGSQL16_DESC=	Use PostgreSQL16 as backend
SQLITE3_DESC=	Use SQLite3 as backend

.include <bsd.port.mk>
.include <bsd.port.options.mk>

.if empty(PORT_OPTIONS:MSQLITE3) && empty(PORT_OPTIONS:MMYSQL80) && \
	!empty(PORT_OPTIONS:MPGSQL16)
USES+=		pgsql
LIB_DEPENDS+=	libpq.so:databases/postgresql16-client
.endif
.if empty(PORT_OPTIONS:MPGSQL16) && empty(PORT_OPTIONS:MMYSQL80) && \
	!empty(PORT_OPTIONS:MSQLITE3)
USES+=		sqlite
LIB_DEPENDS+=	libsqlite3.so:databases/sqlite3
.endif
.if empty(PORT_OPTIONS:MSQLITE3) && empty(PORT_OPTIONS:MPGSQL16) && \
	!empty(PORT_OPTIONS:MMYSQL80)
USES+=		mysql
LIB_DEPENDS+=	libmysqlclient.so:databases/mysql80-client
.endif
