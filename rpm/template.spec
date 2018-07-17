Name:           ros-indigo-novatel-gps-driver
Version:        3.5.0
Release:        0%{?dist}
Summary:        ROS novatel_gps_driver package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       libpcap-devel
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-gps-common
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-novatel-gps-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-swri-math-util
Requires:       ros-indigo-swri-nodelet
Requires:       ros-indigo-swri-roscpp
Requires:       ros-indigo-swri-serial-util
Requires:       ros-indigo-swri-string-util
Requires:       ros-indigo-tf
BuildRequires:  boost-devel
BuildRequires:  libpcap-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-gps-common
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-novatel-gps-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-swri-math-util
BuildRequires:  ros-indigo-swri-nodelet
BuildRequires:  ros-indigo-swri-roscpp
BuildRequires:  ros-indigo-swri-serial-util
BuildRequires:  ros-indigo-swri-string-util
BuildRequires:  ros-indigo-tf

%description
Driver for NovAtel receivers

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jul 17 2018 P. J. Reed <preed@swri.org> - 3.5.0-0
- Autogenerated by Bloom

* Fri Oct 06 2017 P. J. Reed <preed@swri.org> - 3.4.0-0
- Autogenerated by Bloom

* Thu Aug 31 2017 P. J. Reed <preed@swri.org> - 3.3.0-0
- Autogenerated by Bloom

