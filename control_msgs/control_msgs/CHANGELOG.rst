^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package control_msgs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.5.2 (2020-03-11)
------------------
* Bump CMake version to avoid CMP0048 (`#40 <https://github.com/ros-controls/control_msgs/issues/40>`_)
* Contributors: Shane Loretz

1.5.1 (2019-11-27)
------------------
* add description of JointControllerState.msg (`#30 <https://github.com/ros-controls/control_msgs/issues/30>`_)
* Contributors: Shuang Li

1.5.0 (2019-02-19)
------------------
* Adding a JointJog msg
* Replace Adolfo with Bence as maintainer
* Contributors: AndyZe, Bence Magyar

1.4.0 (2016-04-15)
------------------
* Add antiwindup to JointControllerState message definition
* Add PidState message
* Contributors: Paul Bovbel

1.3.1 (2015-03-05)
------------------
* Export architecture_independent flag in package.xml
* Change package maintainer.
* Contributors: Adolfo Rodriguez Tsouroukdissian, Scott K Logan

1.3.0 (2014-02-27)
------------------
* Add error_string to action result.
* Contributors: Adolfo Rodriguez Tsouroukdissian

1.2.0 (2013-04-25)
------------------

1.1.6 (2013-02-11)
------------------
* adds missing feedback field to PointHeadAction
* Contributors: Adam Leeper

1.1.5 (2013-01-23)
------------------
* changes PointHeadAction.action to PointHead.action
* Contributors: Adam Leeper

1.1.4 (2013-01-22)
------------------
* this now contains all messages, services and actions that used to be in ros_controllers and/or pr2_controllers_msgs
* copy JointControllerState and JointTrajectoryControllerState  from pr2_controllers_msgs
* copy GripperCommand from pr2_controllers_msgs
* modified dep type of catkin
* Contributors: Dirk Thomas, Ioan Sucan

1.1.3 (2012-12-13)
------------------
* fix dep
* add missing downstream depend
* switched from langs to message_* packages
* Contributors: Dirk Thomas

1.1.2 (2012-12-03)
------------------

1.1.1 (2012-11-19 15:52)
------------------------
* added metapackage for backward compatibility
* Contributors: Ioan Sucan

1.1.0 (2012-11-19 14:54)
------------------------
* port to catkin
* add bogus dependency on rospy, to get ros_comm
* Added documentation for the FollowJointTrajectory action and the JointTolerance message.
* Added PointHeadAction to control_msgs
* First cut at a FollowJointTrajectory action
* Contributors: Brian Gerkey, Ioan Sucan, Stuart Glaser
