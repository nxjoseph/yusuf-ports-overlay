PORTNAME=	vimpager
DISTVERSION=	2.06.20241028
CATEGORIES=	sysutils

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Use Vim/NeoVim as a pager (${FLAVOR:U} flavor)
WWW=		https://github.com/rkitover/vimpager

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

FLAVORS=	console gtk2 gtk3 motif tiny x11 neovim
FLAVOR?=	${FLAVORS:[1]}

USES=		gmake
USE_GITHUB=	yes
GH_ACCOUNT=	rkitover
GH_TAGNAME=	ce697c4

# Register conflicts with all other flavors
CONFLICTS_INSTALL=	${FLAVORS:N${FLAVOR}:S/^/vimpager-/}

NO_ARCH=	yes

OPTIONS_DEFINE=	DOCS
OPTIONS_SUB=	yes

.include <bsd.port.options.mk>

console_RUN_DEPENDS=	${LOCALBASE}/bin/vim:editors/vim@console
gtk2_PKGNAMESUFFIX=	-gtk2
gtk2_RUN_DEPENDS=	${LOCALBASE}/bin/vim:editors/vim@gtk2
gtk3_PKGNAMESUFFIX=	-gtk3
gtk3_RUN_DEPENDS=	${LOCALBASE}/bin/vim:editors/vim@gtk3
neovim_PKGNAMESUFFIX=	-neovim
neovim_RUN_DEPENDS=	${LOCALBASE}/bin/nvim:editors/neovim
motif_PKGNAMESUFFIX=	-motif
motif_RUN_DEPENDS=	${LOCALBASE}/bin/vim:editors/vim@motif
tiny_PKGNAMESUFFIX=	-tiny
tiny_RUN_DEPENDS=	${LOCALBASE}/bin/vim:editors/vim@tiny
x11_PKGNAMESUFFIX=	-x11
x11_RUN_DEPENDS=	${LOCALBASE}/bin/vim:editors/vim@x11

.include <bsd.port.mk>
