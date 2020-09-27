
#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_.msg import Pose
from math import sqrt, atan2, pi, pow
import numpy as np


def update_pose(msg):
    global pos_msg
    pos_msg = msg
    # pos_msg.x = round(msg.x, 4)
    # pos_msg.y = round(msg.y, 4)

def angular_control(k_angular = 1, k_linear = 1):

    global pos_msg
    global goal_msg
    global vel_msg
    global distance
    global angle


    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    rospy.init_node('square_closeloop')

    vel_msg = Twist()
    pos_msg = Pose()
    rate = rospy.Rate(10)

    goal_msg = Pose()
    goal = np.array([[5, 5], [8, 5], [8, 8], [5, 8], [5, 5]])
    current_angle = np.array([5*pi/4, 2*pi, pi/2, pi, 3*pi/2] )

    for i in range(4):
        goal_msg.x = goal[i][0]
        goal_msg.y = goal[i][1]


        # current_angle =  atan2((goal_msg.y - pos_msg.y), (goal_msg.x - pos_msg.x))
        print(current_angle[i])
        print(goal_msg)
        print(pos_msg)

        angle = abs(current_angle[i] - pos_msg.theta)

        distance = abs(sqrt((goal_msg.x - pos_msg.x)**2 + (goal_msg.y - pos_msg.y)**2))

        while abs(current_angle[i] - pos_msg.theta) >= 0.01:
            print('In angle loop '+ str(goal_msg.theta))
            print('=======================')
            print('In angle floop '+ str(pos_msg.theta))
            print('~~~~~~~~~~~~~~~~~~~~~~~')
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = k_angular * (current_angle[i] - pos_msg.theta)
            velocity_publisher.publish(vel_msg)
            angle = abs(current_angle - pos_msg.theta)
            rate.sleep()

        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

        print('+++++++++++++++++++++++++++++')

        while distance >= 0.1:
            print('In distance loop ' + str(pos_msg.theta))
            print('------------------------')
            print('In distance loop ' + str(goal_msg.theta))
            print('========================')

            vel_msg.linear.x = k_linear * distance
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            distance = sqrt(pow((goal_msg.x - pos_msg.x), 2) + pow((goal_msg.y - pos_msg.y), 2))
            rate.sleep()

        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        print('999999999999999999999999999999')
        # rospy.spin()


if __name__ == '__main__':

    try:
        rospy.init_node('square_closeloop')
        pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, update_pose)

        angular_control()

    except rospy.ROSInterruptException: pass
