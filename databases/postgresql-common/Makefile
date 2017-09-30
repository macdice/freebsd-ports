# $FreeBSD$

PORTNAME=postgresql-common
DISTVERSION=190
CATEGORIES=databases
MASTER_SITES=DEBIAN
MASTER_SITE_SUBDIR=pool/main/p/postgresql-common
DISTNAME=postgresql-common_${PORTVERSION}
WRKSRC=${WRKDIR}/postgresql-common
USES=tar:xz perl5 shebangfix gmake
LICENSE=GPLv2+
SHEBANG_FILES=pg_lsclusters \
	      pg_createcluster \
	      pg_ctlcluster \
	      pg_dropcluster \
	      pg_renamecluster \
	      pg_virtualenv
RUN_DEPENDS=postgresql-client-common=${DISTVERSION}:databases/postgresql-client-common
USERS=postgres
GROUPS=postgres
MAINTAINER=pgsql@freebsd.org
COMMENT=Cluster management for PostgreSQL (WIP port, not yet fully baked)

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/pg_lsclusters ${STAGEDIR}${PREFIX}/bin
	${INSTALL_SCRIPT} ${WRKSRC}/pg_createcluster ${STAGEDIR}${PREFIX}/bin
	${INSTALL_SCRIPT} ${WRKSRC}/pg_dropcluster ${STAGEDIR}${PREFIX}/bin
	${INSTALL_SCRIPT} ${WRKSRC}/pg_ctlcluster ${STAGEDIR}${PREFIX}/bin
	${INSTALL_SCRIPT} ${WRKSRC}/pg_renamecluster ${STAGEDIR}${PREFIX}/bin
	${INSTALL_SCRIPT} ${WRKSRC}/pg_virtualenv ${STAGEDIR}${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/pg_lsclusters.1 ${STAGEDIR}${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/pg_createcluster.1 ${STAGEDIR}${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/pg_dropcluster.1 ${STAGEDIR}${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/pg_ctlcluster.1 ${STAGEDIR}${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/pg_renamecluster.1 ${STAGEDIR}${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/pg_virtualenv.1 ${STAGEDIR}${PREFIX}/man/man1

.include <bsd.port.mk>
