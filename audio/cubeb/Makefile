PORTNAME=	cubeb
DISTVERSION=	g20250212
CATEGORIES=	audio

MAINTAINER=	nxjoseph@protonmail.com
COMMENT=	Cross platform audio library
WWW=		https://github.com/mozilla/cubeb

LICENSE=	ISCL
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		cmake compiler:c++17-lang pkgconfig
USE_GITHUB=	yes
GH_ACCOUNT=	mozilla
GH_TAGNAME=	832fcf3
GH_TUPLE=	google:googletest:40412d8:googletest \
		arsenm:sanitizers-cmake:aab6948:cmake/sanitizers-cmake \
		mozilla:cubeb-coreaudio-rs:8f39e9f:src/cubeb-coreaudio-rs \
		mozilla:cubeb-pulse-rs:6bac666:src/cubeb-pulse-rs

# Do not depend on found audio backends by default
CMAKE_OFF=	-DLAZY_LOAD_LIBS:BOOL=off

# Fix -lsndio not found error
SNDIO_USES=	localbase:ldflags

OPTIONS_DEFINE=		TESTS TOOLS RUST
OPTIONS_DEFAULT=	ALSA JACK OSS PULSEAUDIO SNDIO TESTS TOOLS
OPTIONS_MULTI=		AUDIO
OPTIONS_MULTI_AUDIO=	ALSA JACK OSS PULSEAUDIO SNDIO
OPTIONS_SUB=		yes

TESTS_DESC=	Build tests
TOOLS_DESC=	Build cubeb-test tool
RUST_DESC=	Build rust backends

ALSA_LIB_DEPENDS=	libasound.so:audio/alsa-lib
ALSA_CMAKE_BOOL=	-DUSE_ALSA:BOOL=true
JACK_LIB_DEPENDS=	libjack.so:audio/jack
JACK_CMAKE_BOOL=	-DUSE_JACK:BOOL=true
OSS_CMAKE_BOOL=		-DUSE_OSS:BOOL=true
PULSEAUDIO_LIB_DEPENDS=	libpulse.so:audio/pulseaudio
PULSEAUDIO_CMAKE_BOOL=	-DUSE_PULSE:BOOL=true
SNDIO_LIB_DEPENDS=	libsndio.so:audio/sndio
SNDIO_CMAKE_BOOL=	-DUSE_SNDIO:BOOL=true
TESTS_CMAKE_BOOL=	-DBUILD_TESTS:BOOL=on
TOOLS_LIB_DEPENDS=	libspeexdsp.so:audio/speexdsp
TOOLS_CMAKE_BOOL=	-DBUILD_TOOLS:BOOL=on
RUST_USES=		cargo

post-extract:
	(${MV} ${WRKSRC}/sanitizers-cmake ${WRKSRC}/cmake && \
		${RM} -r ${WRKSRC}/googletest && \
		${LN} -s ${WRKDIR}/googletest-40412d8 ${WRKSRC}/googletest)

.include <bsd.port.mk>
