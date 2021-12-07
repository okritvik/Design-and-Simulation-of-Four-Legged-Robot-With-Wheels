^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package combined_robot_hw
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.19.5 (2021-06-16)
-------------------

0.19.4 (2020-12-05)
-------------------

0.19.3 (2020-10-11)
-------------------

0.19.2 (2020-08-17)
-------------------

0.19.1 (2020-05-10)
-------------------
* Function specifiers noetic (`#453 <https://github.com/ros-controls/ros_control/issues/453>`_)
  * Add override specifiers & default constructors
  * Delete ControllerBase copy & move ctors
  * Remove unnecessary default constructors
  * Modernize additional constructors
  * Revert ImuSensorHandle::Data::Data() = default
  * Remove unnecessary default overridden constructors
  * Remove semicolon after function body
  Co-authored-by: Matt Reynolds <mtreynolds@uwaterloo.ca>
* Use setuptools instead of distutils (`#429 <https://github.com/ros-controls/ros_control/issues/429>`_)
* Contributors: Bence Magyar, Matt Reynolds

0.19.0 (2020-04-23)
-------------------

0.18.0 (2020-04-16)
-------------------
* Bump CMake version to avoid CMP0048 (`#427 <https://github.com/ros-controls/ros_control/issues/427>`_)
* Contributors: Shane Loretz

0.17.0 (2020-02-24)
-------------------
* Use auto keyword
* Use default member initializers
* Improve controller and resource filtering for CombinedRobotHW
* Prefer default member initializers
* Contributors: AbhinavSingh, Bence Magyar, Matt Reynolds, Toni Oliver

0.16.0 (2020-01-27)
-------------------
* Use range-based for loop
* Update dependencies
  - Dependencies needed to compile are <build_depend>
  - Dependencies used in public headers are <build_export_depend>
  - Dependencies needed to link or run are <exec_depend>
* Use #pragma once
* Replace header guard with #pragma once
* Remove unused Boost dependencies
* Apply consistent style to CMakeLists.txt files
* Apply consistent style to package.xml files
* Fix build error in clang error: non-aggregate type 'std::vector' (aka 'vector >') cannot be initialized with an initializer list
* fix install destination
* specify RUNTIME DESTINATION for libraries needed for exporting DLLs on Windows
* Contributors: Bence Magyar, James Xu, Matt Reynolds, Victor Lopez

0.15.1 (2018-09-30)
-------------------

0.15.0 (2018-05-28)
-------------------
* CreateInstance -> CreateUniqueInstance
* boost::shared_ptr -> std::shared_ptr
* Introduce shared_ptr typedefs
* Contributors: Bence Magyar

0.14.2 (2018-04-26)
-------------------
* Update maintainers
* Contributors: Bence Magyar

0.14.1 (2018-04-16)
-------------------

0.14.0 (2018-03-26)
-------------------
* migrate classloader headers
* Contributors: Mathias Lüdtke

0.13.0 (2017-12-23)
-------------------

0.12.0 (2017-08-05)
-------------------

0.11.5 (2017-06-28)
-------------------
* Fix typo in architecture.svg
* Contributors: Martin Günther

0.11.4 (2017-02-14)
-------------------

0.11.3 (2016-12-07)
-------------------

0.11.2 (2016-11-28)
-------------------
* Add Toni's email to the author fields too
* Add Enrique and Bence to maintainer list
* Clean up export leftovers from rosbuild
* Convert to format2, fix dependency in cmake
* Add combined_robot_hw to metapackage & system figure
* Contributors: Bence Magyar

0.11.1 (2016-08-18)
-------------------

0.11.0 (2016-05-23)
-------------------
* Add packages combined_robot_hw and combined_robot_hw_tests. combined_robot_hw allows to load different RobotHW as plugins and combines them into a single RobotHW. A single controller manager can then access resources from any robot.
* Contributors: Toni Oliver

0.10.1 (2016-04-23)
-------------------

0.10.0 (2015-11-20)
-------------------

0.9.4 (2016-02-12)
------------------

0.9.3 (2015-05-05)
------------------

0.9.2 (2015-05-04)
------------------

0.9.1 (2014-11-03)
------------------

0.9.0 (2014-10-31)
------------------

0.8.2 (2014-06-25)
------------------

0.8.1 (2014-06-24)
------------------

0.8.0 (2014-05-12)
------------------

0.7.3 (2014-10-28)
------------------

0.7.2 (2014-04-01)
------------------

0.7.1 (2014-03-31)
------------------

0.7.0 (2014-03-28)
------------------

0.6.0 (2014-02-05)
------------------

0.5.8 (2013-10-11)
------------------

0.5.7 (2013-07-30)
------------------

0.5.6 (2013-07-29)
------------------

0.5.5 (2013-07-23 17:04)
------------------------

0.5.4 (2013-07-23 14:37)
------------------------

0.5.3 (2013-07-22 18:06)
------------------------

0.5.2 (2013-07-22 15:00)
------------------------

0.5.1 (2013-07-19)
------------------

0.5.0 (2013-07-16)
------------------

0.4.0 (2013-06-25)
------------------
