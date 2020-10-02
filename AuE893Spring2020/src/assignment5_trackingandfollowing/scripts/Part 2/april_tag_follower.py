#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from apriltag_ros.msg import AprilTagDetectionArray
tags = []
steer = 0
dist = 0
def call_back(msg):
    global steer
    global dist
    steer = msg.detections[0].pose.pose.pose.position.x
    dist = msg.detections[0].pose.pose.pose.position.z

    # print(msg.detections[0].pose.pose.pose.position)
    # print('fffffffffff')


if __name__ == '__main__':
    # global tags
    rospy.init_node('april_tag_follower', anonymous=True)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray, call_back)
    #tags = AprilTagDetection()
    rate = rospy.Rate(10)
    cmd_vel = Twist()
    p_dist = 0.3
    p_steer = 5
    while not rospy.is_shutdown():

        cmd_vel.angular.z = -steer*p_steer
        if dist < 0.2:
            cmd_vel.linear.x = 0
            pub.publish(cmd_vel)
        else:
            cmd_vel.linear.x = dist*p_dist
            pub.publish(cmd_vel)
        print(steer,"ulalalalala", dist)
        print(cmd_vel)
        rate.sleep()
    rospy.spin()
