# $FreeBSD$

PORTNAME=postgresql-client-common
DISTVERSION=190
CATEGORIES=databases
MASTER_SITES=DEBIAN
MASTER_SITE_SUBDIR=pool/main/p/postgresql-common
DISTNAME=postgresql-common_${PORTVERSION}
WRKSRC=${WRKDIR}/postgresql-common
USES=tar:xz perl5 shebangfix gmake
LICENSE=GPLv2+
SHEBANG_FILES=pg_wrapper
MAINTAINER=pgsql@freebsd.org
COMMENT=Multi-version PostgreSQL client wrappers (WIP port, not yet fully baked)

post-patch:
	${REINPLACE_CMD} -e \
		"s|/etc/|${PREFIX}/etc/|; \
		 s|/usr/lib/|${PREFIX}/lib/|" \
		 ${WRKSRC}/PgCommon.pm

do-install:
	${MKDIR} -p ${STAGEDIR}${PREFIX}/${SITE_PERL_REL}
	${INSTALL_DATA} ${WRKSRC}/PgCommon.pm ${STAGEDIR}${PREFIX}/${SITE_PERL_REL}
	${INSTALL_SCRIPT} ${WRKSRC}/pg_wrapper ${STAGEDIR}${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/pg_wrapper.1 ${STAGEDIR}${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/postgresqlrc.5 ${STAGEDIR}${PREFIX}/man/man5
	${INSTALL_MAN} ${WRKSRC}/user_clusters.5 ${STAGEDIR}${PREFIX}/man/man5
	for f in clusterdb createdb createlang createuser dropdb droplang dropuser \
		pg_basebackup pg_dump pg_dumpall pg_isready pg_recvxlog \
		pg_recvlogical pg_restore pgbench psql reindexdb \
		vacuumdb vacuumlo ; do \
		${RLN} ${STAGEDIR}${PREFIX}/bin/pg_wrapper ${STAGEDIR}${PREFIX}/bin/$$f ; \
	done

.include <bsd.port.mk>
