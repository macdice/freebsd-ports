# Created by: mi@aldan.ziplink.net
# $FreeBSD$

PORTNAME=	xmdiary
PORTVERSION=	3.0.3
PORTREVISION=	5
CATEGORIES=	deskutils
MASTER_SITES=	XCONTRIB/office

MAINTAINER=	mi@aldan.algebra.com
COMMENT=	Personal and group calendar utility

NO_CDROM=	Do not sell for profit
USES=		imake motif
USE_XORG=	x11 xext xp xpm xt

post-patch:
	@${REINPLACE_CMD} -e 's/malloc\.h/stdlib.h/' \
		${WRKSRC}/tools/LstLinked.c ${WRKSRC}/tools/System.c \
		${WRKSRC}/xtools/xitClipboard.c ${WRKSRC}/xtools/xitInfoFile.c
	${REINPLACE_CMD} -e 's|/usr/X11R6|${LOCALBASE}|g' \
		-e 's|CcCmd gcc|CcCmd ${CC}|' '${WRKSRC}/XDiary.tmpl'

.include <bsd.port.mk>
