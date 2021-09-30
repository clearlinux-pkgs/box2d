#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : box2d
Version  : 2.4.1
Release  : 3
URL      : https://github.com/erincatto/box2d/archive/v2.4.1/box2d-2.4.1.tar.gz
Source0  : https://github.com/erincatto/box2d/archive/v2.4.1/box2d-2.4.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: box2d-lib = %{version}-%{release}
Requires: box2d-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
Patch1: 0001-Update-doctest-version.patch

%description
![Box2D Logo](https://box2d.org/images/logo.svg)
# Build Status
[![Build Status](https://travis-ci.org/erincatto/box2d.svg?branch=master)](https://travis-ci.org/erincatto/box2d)

%package dev
Summary: dev components for the box2d package.
Group: Development
Requires: box2d-lib = %{version}-%{release}
Provides: box2d-devel = %{version}-%{release}
Requires: box2d = %{version}-%{release}

%description dev
dev components for the box2d package.


%package lib
Summary: lib components for the box2d package.
Group: Libraries
Requires: box2d-license = %{version}-%{release}

%description lib
lib components for the box2d package.


%package license
Summary: license components for the box2d package.
Group: Default

%description license
license components for the box2d package.


%prep
%setup -q -n box2d-2.4.1
cd %{_builddir}/box2d-2.4.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633045819
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1633045819
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/box2d
cp %{_builddir}/box2d-2.4.1/LICENSE %{buildroot}/usr/share/package-licenses/box2d/bd0acc66ecec5d3dcb01cd1c45d873766fbe93d1
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/box2d/b2_api.h
/usr/include/box2d/b2_block_allocator.h
/usr/include/box2d/b2_body.h
/usr/include/box2d/b2_broad_phase.h
/usr/include/box2d/b2_chain_shape.h
/usr/include/box2d/b2_circle_shape.h
/usr/include/box2d/b2_collision.h
/usr/include/box2d/b2_common.h
/usr/include/box2d/b2_contact.h
/usr/include/box2d/b2_contact_manager.h
/usr/include/box2d/b2_distance.h
/usr/include/box2d/b2_distance_joint.h
/usr/include/box2d/b2_draw.h
/usr/include/box2d/b2_dynamic_tree.h
/usr/include/box2d/b2_edge_shape.h
/usr/include/box2d/b2_fixture.h
/usr/include/box2d/b2_friction_joint.h
/usr/include/box2d/b2_gear_joint.h
/usr/include/box2d/b2_growable_stack.h
/usr/include/box2d/b2_joint.h
/usr/include/box2d/b2_math.h
/usr/include/box2d/b2_motor_joint.h
/usr/include/box2d/b2_mouse_joint.h
/usr/include/box2d/b2_polygon_shape.h
/usr/include/box2d/b2_prismatic_joint.h
/usr/include/box2d/b2_pulley_joint.h
/usr/include/box2d/b2_revolute_joint.h
/usr/include/box2d/b2_rope.h
/usr/include/box2d/b2_settings.h
/usr/include/box2d/b2_shape.h
/usr/include/box2d/b2_stack_allocator.h
/usr/include/box2d/b2_time_of_impact.h
/usr/include/box2d/b2_time_step.h
/usr/include/box2d/b2_timer.h
/usr/include/box2d/b2_types.h
/usr/include/box2d/b2_weld_joint.h
/usr/include/box2d/b2_wheel_joint.h
/usr/include/box2d/b2_world.h
/usr/include/box2d/b2_world_callbacks.h
/usr/include/box2d/box2d.h
/usr/lib64/cmake/box2d/box2dConfig-relwithdebinfo.cmake
/usr/lib64/cmake/box2d/box2dConfig.cmake
/usr/lib64/cmake/box2d/box2dConfigVersion.cmake
/usr/lib64/libbox2d.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbox2d.so.2
/usr/lib64/libbox2d.so.2.4.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/box2d/bd0acc66ecec5d3dcb01cd1c45d873766fbe93d1
