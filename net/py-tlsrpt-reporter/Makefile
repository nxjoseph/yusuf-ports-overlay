PORTNAME=	tlsrpt-reporter
DISTVERSIONPREFIX=	v
DISTVERSION=	0.5.0
CATEGORIES=	net
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Collectd, fetcher and reportd software for SMTP TLS reporting
WWW=		https://github.com/sys4/tlsrpt-reporter

LICENSE=	GPLv3+
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		gmake python:3.7+ shebangfix
USE_GITHUB=	yes
GH_ACCOUNT=	sys4
USE_PYTHON=	flavors

SHEBANG_FILES=	./tlsrpt_reporter/tlsrpt_*.py

NO_ARCH=	yes
NO_BUILD=	yes
NO_INSTALL=	yes

PORTDOCS=	doc/tlsrpt-*.adoc

OPTIONS_DEFINE=		DOCS TESTS
OPTIONS_DEFAULT=	DOCS TESTS
OPTIONS_SUB=		yes

TESTS_DESC=	Install tests

DOCS_BUILD_DEPENDS=	asciidoctor:textproc/rubygem-asciidoctor

do-install:
	${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/tlsrpt_reporter
	(cd ${WRKSRC}/tlsrpt_reporter && \
		${FIND} . -type f -name "tlsrpt_*.py" -exec ${INSTALL_SCRIPT} \
		{} ${STAGEDIR}${PREFIX}/bin/{} \; && \
		${FIND} . -type f -not -name "tlsrpt_*.py" -exec ${INSTALL_DATA} \
		{} ${STAGEDIR}${PYTHON_SITELIBDIR}/tlsrpt_reporter/{} \
		\;)

do-install-DOCS-on:
	(cd ${WRKSRC}/doc && \
		${SETENV} ${MAKE_ENV} ${MAKE_CMD} ${MAKE_ARGS} ${ALL_TARGET} && \
		${INSTALL_MAN} ./*.1 \
		${STAGEDIR}${PREFIX}/share/man/man1)

do-install-TESTS-on:
	${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}/tlsrpt_reporter/tests
	(cd ${WRKSRC}/tests && \
		${FIND} . -type f -exec ${INSTALL_DATA} {} ${STAGEDIR}${PYTHON_SITELIBDIR}/tlsrpt_reporter/tests/{} \
		\;)

.include <bsd.port.mk>
