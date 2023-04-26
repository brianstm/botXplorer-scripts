#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16

class ObstacleDetector:
    def __init__(self):
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.lidar_sub = rospy.Subscriber('/sick_tim_7xx/lidoutputstate', Int16, self.lidar_callback)
        self.twist = Twist()
        self.obstacle_field1 = False
        self.obstacle_field2 = False

    def lidar_callback(self, data):
        field_sets = data.data >> 12 & 0x0FFF
        field_set_2nd_last = (field_sets >> 1) & 0x0F
        field_set_last = field_sets & 0x0F

        if field_set_2nd_last < 10:
            self.obstacle_field2 = True
        else:
            self.obstacle_field2 = False

        if field_set_last < 2:
            self.obstacle_field1 = True
        else:
            self.obstacle_field1 = False

    def drive(self):
        # 3 meters
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
