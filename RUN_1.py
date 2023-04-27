#!/usr/bin/env python

import rospy
from sick_scan.msg import LIDoutputstateMsg
from geometry_msgs.msg import Twist

class ObstacleDetector:
    def __init__(self):
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.lidar_sub = rospy.Subscriber('/sick_tim_7xx/lidoutputstate', LIDoutputstateMsg, self.lidar_callback)
        self.twist = Twist()
        self.obstacle_field1 = False
        self.obstacle_field2 = False

    def lidar_callback(self, data):
        field1Current = data.output_count[0]
        field2Current = data.output_count[1]

        if field1Current > 0:
            self.obstacle_field1 = True
        else:
            self.obstacle_field1 = False

        if field2Current > 0:
            self.obstacle_field2 = True
        else:
            self.obstacle_field2 = False

    def drive(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.obstacle_field1:
                self.twist.linear.x = 0
            elif self.obstacle_field2:
                self.twist.linear.x = 0.5
            else:
                self.twist.linear.x = 0.7

            self.cmd_pub.publish(self.twist)
            rate.sleep()

            while self.obstacle_field1 or self.obstacle_field2:
                rate.sleep()

if __name__ == '__main__':
    rospy.init_node('obstacle_detector', anonymous=True)
    obstacle_detector = ObstacleDetector()
    obstacle_detector.drive()
