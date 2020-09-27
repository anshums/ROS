#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    # node initialization
    rospy.init_node('go_in_circle')
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    vel_msg = Twist()

    vel_msg.linear.x = 10
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.z = 10
    vel_msg.angular.y = 0
    vel_msg.angular.x = 0

    while not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
