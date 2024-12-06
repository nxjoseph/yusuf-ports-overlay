PORTNAME=	drogon
DISTVERSIONPREFIX=	v
DISTVERSION=	1.9.8
CATEGORIES=	www

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	HTTP web application framework
WWW=		https://github.com/drogonframework/drogon

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libjsoncpp.so:devel/jsoncpp

USES=		cmake localbase:ldflags ssl
USE_GITHUB=	yes
GH_ACCOUNT=	drogonframework
GH_TUPLE=	an-tao:trantor:8bf280ba:trantor/trantor

OPTIONS_DEFAULT=	PGSQL16

OPTIONS_MULTI=		SUPPORT
OPTIONS_MULTI_SUPPORT=	BROTLI CTL DOCS EXAMPLES REDIS SPDLOG YAML

OPTIONS_SINGLE=		BACKEND
OPTIONS_SINGLE_BACKEND=	MYSQL80 PGSQL16 SQLITE3

BROTLI_DESC=	Build Brotli
CTL_DESC=	Build drogon_ctl
DOCS_DESC=	Build Doxygen documentation
EXAMPLES_DESC=	Build examples
MYSQL80_DESC=	Use MySQL80 as backend
PGSQL16_DESC=	Use PostgreSQL16 as backend
REDIS_DESC=	Build with redis support
SPDLOG_DESC=	Allow using the spdlog logging library
SQLITE3_DESC=	Use SQLite3 as backend
YAML_DESC=	Build yaml config

.include <bsd.port.mk>
.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MBROTLI}
CMAKE_ARGS+=	-DBUILD_BROTLI=ON
BUILD_DEPENDS+=	brotli:archivers/brotli
LIB_DEPENDS+=	libbrotlicommon.so:archivers/brotli \
		libbrotlidec.so:archivers/brotli
.else
CMAKE_ARGS+=	-DBUILD_BROTLI=OFF
.endif

.if ${PORT_OPTIONS:MCTL}
CMAKE_ARGS+=	-DBUILD_CTL=ON
.else
CMAKE_ARGS+=	-DBUILD_CTL=OFF
.endif

.if ${PORT_OPTIONS:MDOCS}
CMAKE_ARGS+=	-DBUILD_DOC=ON
BUILD_DEPENDS+=	doxygen:devel/doxygen
.else
CMAKE_ARGS+=	-DBUILD_DOC=OFF
.endif

.if ${PORT_OPTIONS:MEXAMPLES}
CMAKE_ARGS+=	-DBUILD_EXAMPLES=ON
.else
CMAKE_ARGS+=	-DBUILD_EXAMPLES=OFF
.endif

.if ${PORT_OPTIONS:MREDIS}
CMAKE_ARGS+=	-DBUILD_ORM=OFF \
		-DBUILD_REDIS=ON
LIB_DEPENDS+=	libhiredis.so:databases/hiredis
.else
CMAKE_ARGS+=	-DBUILD_REDIS=OFF
.endif

.if ${PORT_OPTIONS:MSPDLOG}
CMAKE_ARGS+=	-DBUILD_SPDLOG=ON
LIB_DEPENDS+=	libspdlog.so:devel/spdlog
.else
CMAKE_ARGS+=	-DBUILD_SPDLOG=OFF \
		-DUSE_SUBMODULE=OFF
.endif

.if ${PORT_OPTIONS:MYAML}
CMAKE_ARGS+=	-DBUILD_YAML_CONFIG=ON
LIB_DEPENDS+=	libyaml-cpp.so:devel/yaml-cpp
.else
CMAKE_ARGS+=	-DBUILD_YAML_CONFIG=OFF
.endif

.if empty(PORT_OPTIONS:MSQLITE3) && empty(PORT_OPTIONS:MMYSQL80) && \
	!empty(PORT_OPTIONS:MPGSQL16)
USES+=		pgsql
LIB_DEPENDS+=	libpq.so:databases/postgresql16-client
CMAKE_ARGS+=	-DBUILD_MYSQL=OFF \
		-DBUILD_ORM=OFF \
		-DBUILD_SQLITE=OFF
.endif
.if empty(PORT_OPTIONS:MPGSQL16) && empty(PORT_OPTIONS:MMYSQL80) && \
	!empty(PORT_OPTIONS:MSQLITE3)
USES+=		sqlite
LIB_DEPENDS+=	libsqlite3.so:databases/sqlite3
CMAKE_ARGS+=	-DBUILD_MYSQL=OFF \
		-DBUILD_ORM=OFF \
		-DBUILD_POSTGRESQL=OFF
.endif
.if empty(PORT_OPTIONS:MSQLITE3) && empty(PORT_OPTIONS:MPGSQL16) && \
	!empty(PORT_OPTIONS:MMYSQL80)
USES+=		mysql
LIB_DEPENDS+=	libmysqlclient.so:databases/mysql80-client
CMAKE_ARGS+=	-DBUILD_ORM=OFF \
		-DBUILD_POSTGRESQL=OFF \
		-DBUILD_SQLITE=OFF
.endif
