PORTNAME=	automated-ytdlp-downloader
DISTVERSIONPREFIX=	v
DISTVERSION=	0.0.7_1
CATEGORIES=	www

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	CLI tool for downloading Videos/Audios using yt-dlp from YouTube
WWW=		https://github.com/nxjosephofficial/automated-ytdlp-downloader

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	yt-dlp:www/yt-dlp

USES=		go:1.22,modules

USE_GITHUB=	yes
GH_ACCOUNT=	nxjosephofficial
GH_TUPLE=	adrg:xdg:v0.4.0:adrg_xdg/vendor/github.com/adrg/xdg \
		golang:sys:v0.1.0:golang_sys/vendor/golang.org/x/sys

GO_PKGNAME=	github.com/${GH_ACCOUNT}/${PORTNAME}
GO_BUILDFLAGS=	-ldflags="-s -w" -o ./build/automated-ytdlp-downloader

PLIST_FILES=	bin/automated-ytdlp-downloader

.include <bsd.port.mk>
