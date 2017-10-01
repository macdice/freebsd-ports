# $FreeBSD$

PORTNAME=pspg
DISTVERSION=0.2
CATEGORIES=databases
USE_GITHUB=yes
GH_ACCOUNT=okbob
GH_TAGNAME=v${DISTVERSION}
GNU_CONFIGURE=yes
MAINTAINER=munro@ip9.org
COMMENT=A pager specially designed for PostgreSQL psql

post-patch:
	${REINPLACE_CMD} -e \
		"s|#include <ncurses/curses.h>|#include <ncurses.h>|" \
		${WRKSRC}/src/pspg.c

.include <bsd.port.mk>
