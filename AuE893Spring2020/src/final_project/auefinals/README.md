
## ASSIGNMENT 6: Behaviour planning for autonomous mode switching

<img src="https://github.com/rishabhbhatiamp/ROS/blob/master/AuE893Spring2020/src/final_project/videos/final_project_SLAM.gif" height="400" />

NOTE: To add this package to your own workspace, copy [this](https://github.com/rishabhbhatiamp/ROS/tree/master/AuE893Spring2020/src/final_project/auefinals/turtlebot3_auefinals) folder to the src folder of your workspace and run the below command in the package directory.
```
catkin_make
```
The launch files can be found in the [launch](https://github.com/rishabhbhatiamp/ROS/tree/master/AuE893Spring2020/src/final_project/auefinals/turtlebot3_auefinals/launch) folder

The python script files can be found in the [nodes](https://github.com/rishabhbhatiamp/ROS/tree/master/AuE893Spring2020/src/final_project/auefinals/turtlebot3_auefinals/scripts) folder.

### Description: 

filename: "turtlebot3_autonomy_final.launch"

This file initializes the following nodes:

1. The auefinal world

2. The standing person which will be used for leg tracking

3. The person teleop window

4. Leg detection package

5. Tiny yolo package

6. Main integrated python script for the requirements of the final project: 

NOTE: This component of the launch file has been commented to allow for the world and the several nodes load up correctly. This node can be run manually after everything has loaded to ensure that the bot starts moving only after it can be seen in the world.

7. hector slam navigation package (arg value can be changed to run the other packages if they are installed in your system)

### Running Instructions: 
The command for executing the above launch file is:
```
$ roslaunch turtlebot3_auefinals_pkg turtlebot3_autonomy_final.launch 
```