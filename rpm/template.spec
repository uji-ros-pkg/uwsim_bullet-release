Name:           ros-melodic-uwsim-bullet
Version:        2.82.2
Release:        1%{?dist}
Summary:        ROS uwsim_bullet package

Group:          Development/Libraries
License:        Check author's website
Source0:        %{name}-%{version}.tar.gz

Requires:       freeglut-devel
Requires:       libXext-devel
Requires:       ros-melodic-catkin
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  libXext-devel

%description
The bullet library. See https://code.google.com/p/bullet

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Sun Nov 10 2019 Mario Prats <marioprats@gmail.com> - 2.82.2-1
- Autogenerated by Bloom

* Fri Oct 11 2019 Mario Prats <marioprats@gmail.com> - 2.82.1-1
- Autogenerated by Bloom

