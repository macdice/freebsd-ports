# $FreeBSD$

PORTNAME=	libpq5
DISTVERSION=	10rc1
PORTREVISION=	0
CATEGORIES=	databases
DISTNAME=	postgresql-${DISTVERSION}
MASTER_SITES=	PGSQL/source/v${DISTVERSION}

MAINTAINER=	pgsql@FreeBSD.org
COMMENT=	The libpq5 version from the highest released major version of PostgreSQL

LICENSE=	PostgreSQL

WRKSRC=		${WRKDIR}/postgresql-${DISTVERSION}

USES=		tar:bzip2 gmake
GNU_CONFIGURE=	yes

LDFLAGS+=	-L${LOCALBASE}/lib
INCLUDES+=	-I${LOCALBASE}/include
CONFIGURE_ARGS+=--with-libraries=${PREFIX}/lib \
		--with-includes=${PREFIX}/include \
		--enable-thread-safety
CONFIGURE_ENV+=	INCLUDES="${INCLUDES}" \
		PTHREAD_LIBS="-lpthread" \
		LDFLAGS_SL="${LDFLAGS_SL}"
LDFLAGS+=	-lpthread

INSTALL_DIRS=	src/interfaces
BUILD_DIRS=	src/port ${INSTALL_DIRS}
INSTALL_TARGET=install-strip

do-build:
	cd ${WRKSRC} && cd src/interfaces/libpq && ${SETENV} ${MAKE_ENV} ${MAKE_CMD}

do-install:
	cd ${WRKSRC} && cd src/interfaces/libpq && ${SETENV} ${MAKE_ENV} ${MAKE_CMD} ${INSTALL_TARGET}

OPTIONS_DEFINE+=	SSL
SSL_DESC=	Build with OpenSSL support

OPTIONS_DEFAULT+=	SSL

SSL_USES=	ssl
SSL_CONFIGURE_WITH=openssl

OPTIMIZED_CFLAGS_CFLAGS=	-O3 -funroll-loops

DEBUG_CONFIGURE_ENABLE=	debug

.include <bsd.port.mk>
