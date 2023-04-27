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
        field1Current = data.data[0]
        field2Current = data.data[1]

        if field1Current < 2:
            self.obstacle_field1 = True
        else:
            self.obstacle_field1 = False

        if field2Current < 10:
            self.obstacle_field2 = True
        else:
            self.obstacle_field2 = False

    def drive(self):
        # 3 meters
        rate = rospy.Rate(10)
        start_time = rospy.Time.now()
        distance = 0
        while distance < 3 and not rospy.is_shutdown():
            if self.obstacle_field2:
                self.twist.linear.x = 0.2
            elif self.obstacle_field1:
                self.twist.linear.x = 0
                break
            else:
                self.twist.linear.x = 0.7

            self.cmd_pub.publish(self.twist)
            current_time = rospy.Time.now()
            distance = self.twist.linear.x * (current_time - start_time).to_sec()
            rate.sleep()

        self.twist.linear.x = 0
        self.cmd_pub.publish(self.twist)

if __name__ == '__main__':
    rospy.init_node('obstacle_detector', anonymous=True)
    obstacle_detector = ObstacleDetector()
    obstacle_detector.drive()
