# Created by: Sunpoet Po-Chuan Hsieh <sunpoet@FreeBSD.org>
# $FreeBSD$

PORTNAME=	compass-core
PORTVERSION=	1.0.3
PORTREVISION=	1
CATEGORIES=	textproc ruby
MASTER_SITES=	RG

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Compass core stylesheet library and minimum required ruby extensions

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE.txt

RUN_DEPENDS=	rubygem-multi_json>=1.0:devel/rubygem-multi_json \
		rubygem-sass34>=0:textproc/rubygem-sass34

NO_ARCH=	yes
USE_RUBY=	yes
USES=		gem

.include <bsd.port.mk>
