#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class LidarNav(object):
    def __init__(self):
        rospy.init_node('lidar_nav')

        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)

        self.rate = rospy.Rate(10) # 10 Hz
        self.speed = 0.5 # m/s
        self.slowdown_distance = 0.5 # meters
        self.stop_distance = 0.1 # meters

    def scan_callback(self, msg):
        # Calculate the minimum distance to an obstacle in front of the robot
        distances = msg.ranges[0:180] # only consider the front half of the scan
        min_distance = min(distances)

        # Adjust the robot's speed based on the distance to the nearest obstacle
        if min_distance <= self.stop_distance:
            self.cmd_vel_pub.publish(Twist()) # stop the robot
        elif min_distance <= self.slowdown_distance:
            self.cmd_vel_pub.publish(Twist(linear=rospy.get_param('speed', self.speed) * min_distance / self.slowdown_distance)) # slow down
        else:
            self.cmd_vel_pub.publish(Twist(linear=rospy.get_param('speed', self.speed))) # full speed

    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == '__main__':
    node = LidarNav()
    node.run()
