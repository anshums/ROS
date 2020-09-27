Assignment-5: Tracking and Following

Team Members: Ankit Verma, Anshuman Sharma, Prateek Sharma, Rishabh Bhatia, Shaurya Panthri

Member Contributions:
Ankit Verma - Camera Calibration, Shaurya Panthri - April Tag dependency installation in the system, Ankit and Shaurya - Figuring out the changes for topic conversion for raspicam, Rishabh Bhatia - Understanding the base code for line following and implementing the controller and creating the final launch files, Prateek Sharma and Anshuman Sharma - Implementation
of the line following code in the real turtlebot3 - burger and code for april-tag detection and following.Whole team created the readme file collectively for this project as the input from each team memnber was required.

Files included: 
Launch Files in 'launch' folder:
1. task_1_follow_line_gazebo.launch
2. task_1_follow_line_real_world.launch
3. task_2_april_tag.launch

Python Files in 'scripts' folder:
1. follow_line_step_hsv.py
2. follow_line_step_hsv_real_world.py
3. line_follower_basics.py
4. line_follower_basics_real_world.py
5. move_robot.py
6. move_robot_real_world.py

Part 1: Line Following
Description: In this task turtlebot3 burger has to follow a yellow path (try to stay in between the yellow path). This was done in the gazebo simulated environment. We used open CV2 library for image detection. The same task was also performed with modification in color detection in the actual trutlebot3 - burger. For real world, a white path made of A4 sized papers was utilized.

Gazebo: Follow the instructions below for running the simulation of line following problem.
Steps to launch:
1. Open the terminal (cntrl + alt + T)
2. $ roslaunch assignment5_trackingandfollowing task_1_follow_line_gazebo.launch

Real World: Follow the instructions below for running the simulation of line following problem.
Steps to launch:
1. Open the terminal (cntrl + alt + T)
2. $ roscore
3. In a new terminal (cntrl + shift + T)
4. $ ssh pi@{ip_address_of_turtlebot}
5. $ roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch 
6. In a new terminal (cntrl + shift + T)
7. $ ssh pi@{ip_address_of_turtlebot}
8. $ roslaunch turtlebot3_bringup turtlebot3_robot.launch
9. In a new terminal (cntrl + shift + T)
10. $ rosrun image_transport republish compressed in:=raspicam_node/image raw out:=raspicam_node/image_raw
11. In a new terminal (cntrl + shift + T)
12. $ roslaunch assignment5_trackingandfollowing task_1_follow_line_real_world.launch


Part 2: April Tag following:
Description: In this task trutlebot3-burger and Raspberry Pi Camera Module v2 were used. The camera was first mounted on the bot and connected it. Then the camera calibration steps were performed.Later, we used april-tags for april-tag following and detection.  Since the april-tag no. 4 was in the center, we tried following the 4th april-tag in the set of april-tags.To achieve this required april-tag libraries were installed from git-hub. 

Steps to launch:
1. Open the terminal (cntrl + alt + T)
2. $ roscore
3. In a new terminal (cntrl + shift + T)
4. $ ssh pi@{ip_address_of_turtlebot}
5. $ roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch 
6. In a new terminal (cntrl + shift + T)
7. $ ssh pi@{ip_address_of_turtlebot}
8. $ roslaunch turtlebot3_bringup turtlebot3_robot.launch
9. In a new terminal (cntrl + shift + T)
10. $ rosrun image_transport republish compressed in:=raspicam_node/image raw out:=raspicam_node/image_raw
11. In a new terminal (cntrl + shift + T)
12. $ roslaunch assignment5_trackingandfollowing task_2_april_tag.launch 
