PORTNAME=	html2rss
DISTVERSION=	1.0.2
CATEGORIES=	www
MASTER_SITES=	GH

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Create RSS Feeds from HTML pages
WWW=		https://github.com/nxjosephofficial/html2rss

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	gsed:textproc/gsed

USE_GITHUB=	yes
GH_ACCOUNT=	nxjosephofficial

NO_BUILD=	yes

PLIST_FILES=	bin/${PORTNAME} \
		share/man/man8/${PORTNAME}.8.gz

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/${PORTNAME} \
		${STAGEDIR}${PREFIX}/bin/${PORTNAME}
	${INSTALL_MAN} ${WRKSRC}/${PORTNAME}.8 \
		${STAGEDIR}${PREFIX}/share/man/man8

.include <bsd.port.mk>
