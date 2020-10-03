
## ASSIGNMENT 3: Basics of TurtleBot navigation in Gazebo

NOTE: To add this package to your own workspace, copy [this](https://github.com/rishabhbhatiamp/ROS/tree/master/AuE893Spring2020/src/assignment3_turtlebot3) folder to the src folder of your workspace and run the below command in the package directory. This package comtains basic movement examples of the TurtleBot Burger robot in Gazebo.

```
$ catkin_make
```

This assignment package has two launch files:

**1. move.launch**

- This file initializes an empty world in gazebo
- It launches nodes for moving the robot in a circlular or square motion depending on the argument provided while executing the launch command.
- The command for execution with circular motion is: 
```
$ roslaunch assignment3_pkg move.launch code:=circle
```
<img src="https://github.com/rishabhbhatiamp/ROS/blob/master/AuE893Spring2020/src/assignment3_turtlebot3/videos/TurtleBot/circle.gif" height="400" />

- The command for execution with open loop square motion is: 
```
$ roslaunch assignment3_pkg move.launch code:=square
```
<img src="https://github.com/rishabhbhatiamp/ROS/blob/master/AuE893Spring2020/src/assignment3_turtlebot3/videos/TurtleBot/square.gif" height="400" />

**2. turtlebot3_wall.launch**

- This file initializes a world based on the empty world environment.

- This world has a wall in the path of the turtlebot

- This file also launches the python node which executed the desired wall detection and stopping behavior of the turtlebot

- The command for execution of this launch file is:
```
$ roslaunch assignment3_pkg turtlebot3_wall.launch
```
<img src="https://github.com/rishabhbhatiamp/ROS/blob/master/AuE893Spring2020/src/assignment3_turtlebot3/videos/TurtleBot/wall_detection.gif" height="400" />