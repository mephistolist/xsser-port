PORTNAME=	xsser
PORTVERSION=	1.8.4
CATEGORIES=	security
MASTER_SITES=	https://teamsloth.net/

MAINTAINER=	cloneozone@gmail.com
COMMENT=	XSS Exploration
WWW=		https://xsser.03c8.net

LICENSE=	GPLv3

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pycurl>0:ftp/py-pycurl@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pygeoip>0:net/py-pygeoip@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}gobject3>0:devel/py-gobject3@${PY_FLAVOR} \
		pygobject3-common>0:devel/pygobject3-common \
		${PYTHON_PKGNAMEPREFIX}beautifulsoup>0:www/py-beautifulsoup@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}cairocffi>0:graphics/py-cairocffi@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pillow>0:graphics/py-pillow@${PY_FLAVOR}

FLAVORS=	py39
FLAVOR?=	py39

USES=		python desktop-file-utils
USE_PYTHON=	autoplist concurrent distutils allflavors

GH_ACCOUNT=	mephistolist
GH_PROJECT=	xsser-port
GH_TAGNAME=	v${PORTVERSION}

.include <bsd.port.mk>
