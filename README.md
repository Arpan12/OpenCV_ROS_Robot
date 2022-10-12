## OpenCV_ROS_Robot

This is a ROS project to simulate a self driving car environment and test your Computer Vision algorithm.

* To use this Repo

git clone https://github.com/Arpan12/OpenCV_ROS_Robot.git

catkin_make

#### To run commit :dbf4ea4686bd2aa1a4ae40b631fe857531f98981

* In first terminal:

source devel/setup.bash

roslaunch robot_description base_gazebo_control.launch

* In second Terminal:

rosrun rqt_robot_steering rqt_robot_steering
