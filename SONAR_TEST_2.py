#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range

def sonar_callback(data):
    if data.range < 0.5: 
        twist_cmd.linear.x = 0.0
    else:
        twist_cmd.linear.x = 0.7

rospy.init_node('ubiquity_controller_sonars')
rospy.Subscriber('/sonars', Range, sonar_callback)

twist_cmd = Twist()
twist_cmd.linear.x = 0.7
twist_cmd.linear.y = 0.0
twist_cmd.linear.z = 0.0
twist_cmd.angular.x = 0.0
twist_cmd.angular.y = 0.0
twist_cmd.angular.z = 0.0

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    pub.publish(twist_cmd)
    rate.sleep()
