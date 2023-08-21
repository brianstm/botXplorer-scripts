#!/usr/bin/env python

import rospy
from std.msgs.msg import String
from sensor_msgs.msg import Range


def sonar_callback(data):
    sonar_id = data.header.frame_id
    sonar_range = data.range

    if sonar_range < 0.3:
        rospy.loginfo("Obstacle detected, Stop the AMR!", sonar_id)
        stop_pub = rospy.Publisher('/cmd_vel', String, queue_size=10)
        # stop_pub.publish('0 0')
        stop_pub.publish('stop')
    else:
        rospy.loginfo("No obstacle detected, keep going!", sonar_id)
        go_pub = rospy.Publisher('/cmd_vel', String, queue_size=10)
        # go_pub.publish('0.7 0')
        go_pub.publish('linear 0.7')


def listener():
    rospy.init_node('ubiquity_controller_sonars', anynomous=True)
    rospy.Subscriber('/sonars', Range, sonar_callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass