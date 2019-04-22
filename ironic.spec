#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : ironic
Version  : 12.1.0
Release  : 11
URL      : https://tarballs.openstack.org/ironic/ironic-12.1.0.tar.gz
Source0  : https://tarballs.openstack.org/ironic/ironic-12.1.0.tar.gz
Source99 : https://tarballs.openstack.org/ironic/ironic-12.1.0.tar.gz.asc
Summary  : OpenStack Bare Metal Provisioning
Group    : Development/Tools
License  : Apache-2.0
Requires: ironic-bin = %{version}-%{release}
Requires: ironic-config = %{version}-%{release}
Requires: ironic-license = %{version}-%{release}
Requires: ironic-python = %{version}-%{release}
Requires: ironic-python3 = %{version}-%{release}
Requires: Jinja2
Requires: SQLAlchemy
Requires: WSME
Requires: WebOb
Requires: alembic
Requires: automaton
Requires: eventlet
Requires: futurist
Requires: ironic-lib
Requires: jsonpatch
Requires: jsonschema
Requires: keystoneauth1
Requires: keystonemiddleware
Requires: openstacksdk
Requires: os-traits
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.context
Requires: oslo.db
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.middleware
Requires: oslo.policy
Requires: oslo.reports
Requires: oslo.rootwrap
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.upgradecheck
Requires: oslo.utils
Requires: oslo.versionedobjects
Requires: osprofiler
Requires: pbr
Requires: pecan
Requires: psutil
Requires: pysendfile
Requires: python-cinderclient
Requires: python-glanceclient
Requires: python-neutronclient
Requires: python-swiftclient
Requires: pytz
Requires: requests
Requires: retrying
Requires: rfc3986
Requires: six
Requires: stevedore
Requires: tooz
BuildRequires : WSME
BuildRequires : WSME-python
BuildRequires : automaton-python
BuildRequires : buildreq-distutils3
BuildRequires : ironic-lib-python
BuildRequires : jsonpatch
BuildRequires : jsonpatch-python
BuildRequires : keystonemiddleware
BuildRequires : openstacksdk-python
BuildRequires : os-traits-python
BuildRequires : oslo.db-python
BuildRequires : oslo.policy-python
BuildRequires : oslo.reports-python
BuildRequires : oslo.rootwrap-python
BuildRequires : oslo.upgradecheck-python
BuildRequires : oslo.versionedobjects
BuildRequires : osprofiler
BuildRequires : osprofiler-python
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : psutil-python
BuildRequires : py-python
BuildRequires : pysendfile-python
BuildRequires : pytest
BuildRequires : python-cinderclient-python
BuildRequires : python-glanceclient-python
BuildRequires : python-neutronclient-python
BuildRequires : python-swiftclient-python
BuildRequires : retrying
BuildRequires : retrying-python
BuildRequires : tooz
BuildRequires : tooz-python
BuildRequires : tox
BuildRequires : virtualenv

%description
Please see https://alembic.readthedocs.org/en/latest/index.html for general documentation

%package bin
Summary: bin components for the ironic package.
Group: Binaries
Requires: ironic-config = %{version}-%{release}
Requires: ironic-license = %{version}-%{release}

%description bin
bin components for the ironic package.


%package config
Summary: config components for the ironic package.
Group: Default

%description config
config components for the ironic package.


%package license
Summary: license components for the ironic package.
Group: Default

%description license
license components for the ironic package.


%package python
Summary: python components for the ironic package.
Group: Default
Requires: ironic-python3 = %{version}-%{release}

%description python
python components for the ironic package.


%package python3
Summary: python3 components for the ironic package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ironic package.


%prep
%setup -q -n ironic-12.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555949059
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ironic
cp LICENSE %{buildroot}/usr/share/package-licenses/ironic/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ironic-api
/usr/bin/ironic-api-wsgi
/usr/bin/ironic-conductor
/usr/bin/ironic-dbsync
/usr/bin/ironic-rootwrap
/usr/bin/ironic-status

%files config
%defattr(-,root,root,-)
%config /usr/etc/ironic/rootwrap.conf
%config /usr/etc/ironic/rootwrap.d/ironic-images.filters
%config /usr/etc/ironic/rootwrap.d/ironic-lib.filters
%config /usr/etc/ironic/rootwrap.d/ironic-utils.filters

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ironic/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
