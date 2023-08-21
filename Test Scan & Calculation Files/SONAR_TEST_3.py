#!/usr/bin/env python

import rospy
from std.msgs.msg import String
from sensor_msgs.msg import Range


def callback(data):
    if data.header.frame_id == "sonar_0" or data.header.frame_id == "sonar_3" or data.header.frame_id == "sonar_4":
        if data.range < 0.5:
            rospy.loginfo("Obstacle detected")
            cmd_vel_pub.publish('0 0')
        else:
            cmd_vel_pub.publish('0.7 0')


def listener():
    rospy.init_node('ubiquity_controller_sonars', anynomous=True)
    rospy.Subscriber('/sonars', Range, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        cmd_vel_pub = rospy.Publisher('/cmd_vel', String, queue_size=10)
        listener()
    except rospy.ROSInterruptException:
        pass
