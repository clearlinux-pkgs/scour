#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scour
Version  : 0.37
Release  : 11
URL      : https://github.com/scour-project/scour/archive/v0.37/scour-0.37.tar.gz
Source0  : https://github.com/scour-project/scour/archive/v0.37/scour-0.37.tar.gz
Summary  : Scour SVG Optimizer
Group    : Development/Tools
License  : Apache-2.0
Requires: scour-bin = %{version}-%{release}
Requires: scour-license = %{version}-%{release}
Requires: scour-python = %{version}-%{release}
Requires: scour-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
# Scour
[![PyPI](https://img.shields.io/pypi/v/scour.svg)](https://pypi.python.org/pypi/scour "Package listing on PyPI")
[![Build status](https://img.shields.io/travis/scour-project/scour.svg)](https://travis-ci.org/scour-project/scour "Build status (via TravisCI)")
[![Codecov](https://img.shields.io/codecov/c/github/scour-project/scour.svg)](https://codecov.io/gh/scour-project/scour "Code coverage (via Codecov)")

%package bin
Summary: bin components for the scour package.
Group: Binaries
Requires: scour-license = %{version}-%{release}

%description bin
bin components for the scour package.


%package license
Summary: license components for the scour package.
Group: Default

%description license
license components for the scour package.


%package python
Summary: python components for the scour package.
Group: Default
Requires: scour-python3 = %{version}-%{release}

%description python
python components for the scour package.


%package python3
Summary: python3 components for the scour package.
Group: Default
Requires: python3-core
Provides: pypi(scour)
Requires: pypi(six)

%description python3
python3 components for the scour package.


%prep
%setup -q -n scour-0.37
cd %{_builddir}/scour-0.37

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589494895
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scour
cp %{_builddir}/scour-0.37/LICENSE %{buildroot}/usr/share/package-licenses/scour/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/scour

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scour/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
