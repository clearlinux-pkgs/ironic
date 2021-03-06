#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : ironic
Version  : 15.2.0
Release  : 29
URL      : https://tarballs.openstack.org/ironic/ironic-15.2.0.tar.gz
Source0  : https://tarballs.openstack.org/ironic/ironic-15.2.0.tar.gz
Source1  : https://tarballs.openstack.org/ironic/ironic-15.2.0.tar.gz.asc
Summary  : OpenStack Bare Metal Provisioning
Group    : Development/Tools
License  : Apache-2.0
Requires: ironic-bin = %{version}-%{release}
Requires: ironic-data = %{version}-%{release}
Requires: ironic-license = %{version}-%{release}
Requires: ironic-python = %{version}-%{release}
Requires: ironic-python3 = %{version}-%{release}
Requires: Jinja2
Requires: SQLAlchemy
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
Requires: stevedore
Requires: tooz
BuildRequires : Jinja2
BuildRequires : SQLAlchemy
BuildRequires : WebOb
BuildRequires : alembic
BuildRequires : automaton
BuildRequires : buildreq-distutils3
BuildRequires : eventlet
BuildRequires : futurist
BuildRequires : ironic-lib
BuildRequires : jsonpatch
BuildRequires : jsonschema
BuildRequires : keystoneauth1
BuildRequires : keystonemiddleware
BuildRequires : openstacksdk
BuildRequires : os-traits
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.db
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.middleware
BuildRequires : oslo.policy
BuildRequires : oslo.reports
BuildRequires : oslo.rootwrap
BuildRequires : oslo.serialization
BuildRequires : oslo.service
BuildRequires : oslo.upgradecheck
BuildRequires : oslo.utils
BuildRequires : oslo.versionedobjects
BuildRequires : osprofiler
BuildRequires : pbr
BuildRequires : pecan
BuildRequires : pluggy
BuildRequires : psutil
BuildRequires : py-python
BuildRequires : pysendfile
BuildRequires : pytest
BuildRequires : python-cinderclient
BuildRequires : python-glanceclient
BuildRequires : python-neutronclient
BuildRequires : python-swiftclient
BuildRequires : pytz
BuildRequires : requests
BuildRequires : retrying
BuildRequires : rfc3986
BuildRequires : stevedore
BuildRequires : tooz
BuildRequires : tooz-python
BuildRequires : tox
BuildRequires : virtualenv

%description
Ironic
        ======
        
        Team and repository tags
        ------------------------

%package bin
Summary: bin components for the ironic package.
Group: Binaries
Requires: ironic-data = %{version}-%{release}
Requires: ironic-license = %{version}-%{release}

%description bin
bin components for the ironic package.


%package data
Summary: data components for the ironic package.
Group: Data

%description data
data components for the ironic package.


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
Provides: pypi(ironic)
Requires: pypi(alembic)
Requires: pypi(automaton)
Requires: pypi(eventlet)
Requires: pypi(futurist)
Requires: pypi(ironic_lib)
Requires: pypi(jinja2)
Requires: pypi(jsonpatch)
Requires: pypi(jsonschema)
Requires: pypi(keystoneauth1)
Requires: pypi(keystonemiddleware)
Requires: pypi(openstacksdk)
Requires: pypi(os_traits)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.config)
Requires: pypi(oslo.context)
Requires: pypi(oslo.db)
Requires: pypi(oslo.log)
Requires: pypi(oslo.messaging)
Requires: pypi(oslo.middleware)
Requires: pypi(oslo.policy)
Requires: pypi(oslo.rootwrap)
Requires: pypi(oslo.serialization)
Requires: pypi(oslo.service)
Requires: pypi(oslo.upgradecheck)
Requires: pypi(oslo.utils)
Requires: pypi(oslo.versionedobjects)
Requires: pypi(osprofiler)
Requires: pypi(pbr)
Requires: pypi(pecan)
Requires: pypi(psutil)
Requires: pypi(pysendfile)
Requires: pypi(python_cinderclient)
Requires: pypi(python_glanceclient)
Requires: pypi(python_neutronclient)
Requires: pypi(python_swiftclient)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(retrying)
Requires: pypi(rfc3986)
Requires: pypi(sqlalchemy)
Requires: pypi(stevedore)
Requires: pypi(tooz)
Requires: pypi(webob)

%description python3
python3 components for the ironic package.


%prep
%setup -q -n ironic-15.2.0
cd %{_builddir}/ironic-15.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597855466
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ironic
cp %{_builddir}/ironic-15.2.0/LICENSE %{buildroot}/usr/share/package-licenses/ironic/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/ironic
mv %{buildroot}/usr/etc/ironic  %{buildroot}/usr/share/defaults/ironic
## install_append end

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

%files data
%defattr(-,root,root,-)
/usr/share/defaults/ironic/ironic/rootwrap.conf
/usr/share/defaults/ironic/ironic/rootwrap.d/ironic-images.filters
/usr/share/defaults/ironic/ironic/rootwrap.d/ironic-utils.filters

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ironic/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
