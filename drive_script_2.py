#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ObstacleDetector:
    def __init__(self):
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.twist = Twist()
        self.obstacle_field1 = False
        self.obstacle_field2 = False

    def scan_callback(self, data):
        ranges = data.ranges
        field1_ranges = ranges[:10] + ranges[-10:]
        field2_ranges = ranges[45:55]

        if min(field1_ranges) < 0.1:
            self.obstacle_field1 = True
        else:
            self.obstacle_field1 = False

        if min(field2_ranges) < 0.5:
            self.obstacle_field2 = True
        else:
            self.obstacle_field2 = False

    def drive(self):
        rate = rospy.Rate(10)
        start_time = rospy.Time.now()
        distance = 0
        while distance < 3 and not rospy.is_shutdown():
            self.twist.linear.x = 0.5
            self.cmd_pub.publish(self.twist)
            current_time = rospy.Time.now()
            distance = self.twist.linear.x * (current_time - start_time).to_sec()
            rate.sleep()

            if self.obstacle_field2:
                self.twist.linear.x = 0.2
                self.cmd_pub.publish(self.twist)

            if self.obstacle_field1:
                self.twist.linear.x = 0
                self.cmd_pub.publish(self.twist)
                break

        self.twist.linear.x = 0
        self.cmd_pub.publish(self.twist)

if __name__ == '__main__':
    rospy.init_node('obstacle_detector', anonymous=True)
    obstacle_detector = ObstacleDetector()
    obstacle_detector.drive()
