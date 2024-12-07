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

OPTIONS_DEFAULT=	PGSQL

OPTIONS_MULTI=		SUPPORT
OPTIONS_MULTI_SUPPORT=	BROTLI CTL DOCS EXAMPLES REDIS SPDLOG YAML

OPTIONS_SINGLE=		BACKEND
OPTIONS_SINGLE_BACKEND=	MYSQL PGSQL SQLITE

BROTLI_DESC=	Build Brotli
CTL_DESC=	Build drogon_ctl
DOCS_DESC=	Build Doxygen documentation
EXAMPLES_DESC=	Build examples
MYSQL_DESC=	Use MySQL as backend
PGSQL_DESC=	Use PostgreSQL as backend
REDIS_DESC=	Build with redis support
SPDLOG_DESC=	Allow using the spdlog logging library
SQLITE_DESC=	Use SQLite as backend
YAML_DESC=	Build yaml config

BROTLI_BUILD_DEPENDS+=	brotli:archivers/brotli
BROTLI_LIB_DEPENDS+=	libbrotlicommon.so:archivers/brotli \
			libbrotlidec.so:archivers/brotli \
			libbrotlienc.so:archivers/brotli
BROTLI_CMAKE_ON+=	-DBUILD_BROTLI=ON

CTL_CMAKE_ON+=	-DBUILD_CTL=ON

DOCS_BUILD_DEPENDS+=	doxygen:devel/doxygen
DOCS_CMAKE_ON+=		-DBUILD_DOC=ON

EXAMPLES_CMAKE_ON+=	-DBUILD_EXAMPLES=ON

MYSQL_USES+=		mysql
MYSQL_CMAKE_OFF+=	-DBUILD_ORM=OFF \
			-DBUILD_POSTGRESQL=OFF \
			-DBUILD_SQLITE=OFF

PGSQL_USES+=		pgsql
PGSQL_CMAKE_OFF+=	-DBUILD_MYSQL=OFF \
			-DBUILD_ORM=OFF \
			-DBUILD_SQLITE=OFF

REDIS_LIB_DEPENDS+=	libhiredis.so:databases/hiredis
REDIS_CMAKE_ON+=	-DBUILD_REDIS=ON
REDIS_CMAKE_OFF+=	-DBUILD_ORM=OFF

SPDLOG_LIB_DEPENDS+=	libfmt.so:devel/libfmt \
			libspdlog.so:devel/spdlog
SPDLOG_CMAKE_ON+=	-DUSE_SPDLOG=ON

SQLITE_USES+=		sqlite
SQLITE_CMAKE_OFF+=	-DBUILD_MYSQL=OFF \
			-DBUILD_ORM=OFF \
			-DBUILD_POSTGRESQL=OFF

YAML_LIB_DEPENDS+=	libyaml-cpp.so:devel/yaml-cpp
YAML_CMAKE_ON+=		-DBUILD_YAML_CONFIG=ON

.include <bsd.port.options.mk>
.include <bsd.port.mk>
