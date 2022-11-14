## OpenCV_ROS_Robot

This is a ROS project to simulate a self driving car environment and test your Computer Vision algorithm.

![ROS World OpenCV](https://user-images.githubusercontent.com/24242250/201715522-d3d7436f-2d0b-4a08-a8fe-70db1690d14b.png)

![ROS_World](https://user-images.githubusercontent.com/24242250/201715667-fc659b28-c41a-4583-8a53-5caf93f4315f.png)

* To use this Repo

    git clone https://github.com/Arpan12/OpenCV_ROS_Robot.git

    catkin_make
    
    


#### To run commit : d80d56e0a33bf7eccb57a6eef3ddf3970be45e34 (latest)
* In first terminal:

    source devel/setup.bash

    roslaunch robot_description base_gazebo_control_xacro.launch

* In second Terminal:

    rosrun rqt_robot_steering rqt_robot_steering
    
* In Third terminal:

    rosrun robot_description opencv.py




#### To run commit :dbf4ea4686bd2aa1a4ae40b631fe857531f98981

* In first terminal:

    source devel/setup.bash

    roslaunch robot_description base_gazebo_control.launch

* In second Terminal:

    rosrun rqt_robot_steering rqt_robot_steering
    
    

