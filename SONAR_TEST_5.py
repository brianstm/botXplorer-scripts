#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

class ObstacleDetector:
    def __init__(self):
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sonar_sub = rospy.Subscriber('/sonars', Range, self.sonar_callback)
        self.twist = Twist()
        self.obstacle_detected = False

    def sonar_callback(self, data):
        if data.range < 0.3:
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

    def drive(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.obstacle_detected:
                self.twist.linear.x = 0.0
            else:
                self.twist.linear.x = 0.7

            self.cmd_pub.publish(self.twist)
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('obstacle_detector', anonymous=True)
    obstacle_detector = ObstacleDetector()
    obstacle_detector.drive()
