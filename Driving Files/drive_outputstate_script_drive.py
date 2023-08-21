#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32

class ObstacleDetector:
    def __init__(self):
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.state_sub = rospy.Subscriber('/sick_tim_7xx/lidoutputstate', Int32, self.state_callback)
        self.twist = Twist()
        self.last_state = 0
        self.current_state = 0

    def state_callback(self, data):
        self.last_state = self.current_state
        self.current_state = data.data

    def drive(self):
        # Run at constant speed.
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.twist.linear.x = 0.5
            self.cmd_pub.publish(self.twist)

            if self.current_state == 13:
                self.twist.linear.x = 0.2
                self.cmd_pub.publish(self.twist)

            if self.current_state == 14:
                self.twist.linear.x = 0
                self.cmd_pub.publish(self.twist)
                break

            rate.sleep()

        self.twist.linear.x = 0
        self.cmd_pub.publish(self.twist)

if __name__ == '__main__':
    rospy.init_node('obstacle_detector', anonymous=True)
    obstacle_detector = ObstacleDetector()
    obstacle_detector.drive()
