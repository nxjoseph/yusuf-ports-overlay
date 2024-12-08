PORTNAME=	cliwrap
DISTVERSION=	0.9.2
CATEGORIES=	sysutils

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Get Spotify Wrapped for your terminal!
WWW=		https://github.com/islemci/cliwrap

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	bash:shells/bash

USES=		shebangfix
USE_GITHUB=	yes
GH_ACCOUNT=	islemci

SHEBANG_FILES=	./${PORTNAME}

NO_ARCH=	yes
NO_BUILD=	yes

PLIST_FILES=	bin/${PORTNAME}

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/${PORTNAME} \
		${STAGEDIR}${PREFIX}/bin/${PORTNAME}

.include <bsd.port.mk>
