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
        rospy.logdebug('Received laser scan data')
        # Calculate the minimum distance to an obstacle in front of the robot
        distances = msg.ranges[0:180] # only consider the front half of the scan
        min_distance = min(distances)

        rospy.logdebug('Minimum distance to obstacle: {:.2f} meters'.format(min_distance))

        # Adjust the robot's speed based on the distance to the nearest obstacle
        if min_distance <= self.stop_distance:
            rospy.loginfo('Stopping robot')
            self.cmd_vel_pub.publish(Twist()) # stop the robot
        elif min_distance <= self.slowdown_distance:
            rospy.loginfo('Slowing down robot')
            speed = rospy.get_param('speed', self.speed) * min_distance / self.slowdown_distance
            self.cmd_vel_pub.publish(Twist(linear=speed)) # slow down
        else:
            rospy.loginfo('Moving robot at full speed')
            speed = rospy.get_param('speed', self.speed)
            self.cmd_vel_pub.publish(Twist(linear=speed)) # full speed

    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == '__main__':
    rospy.loginfo('Starting lidar_nav node')
    node = LidarNav()
    node.run()
