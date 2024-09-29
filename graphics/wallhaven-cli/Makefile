PORTNAME=	wallhaven-cli
DISTVERSIONPREFIX=	v
DISTVERSION=	1.0.6
CATEGORIES=	graphics

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	CLI for wallhaven that allows you to browse wallpapers in terminal
WWW=		https://github.com/r3tr0ananas/wallhaven-cli

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	chafa:graphics/chafa \
		fzf:textproc/fzf

USES=		go:1.23
USE_GITHUB=	yes
GH_ACCOUNT=	r3tr0ananas
GH_TUPLE=	BurntSushi:toml:v1.4.0:burntsushi_toml/vendor/github.com/BurntSushi/toml \
		inconshreveable:mousetrap:v1.1.0:inconshreveable_mousetrap/vendor/github.com/inconshreveable/mousetrap \
		spf13:cobra:v1.8.1:spf13_cobra/vendor/github.com/spf13/cobra \
		spf13:pflag:v1.0.5:spf13_pflag/vendor/github.com/spf13/pflag

GO_MODULE=	github.com/r3tr0ananas/wallhaven-cli
GO_TARGET=	./wallhaven
GO_BUILDFLAGS=	-ldflags="-s -w"

PLIST_FILES=	bin/wallhaven

.include <bsd.port.mk>
