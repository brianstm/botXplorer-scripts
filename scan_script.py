#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(scan):
    for i, r in enumerate(scan.ranges):
        print(f"Range[{i}]: {r:.2f}  Intensity[{i}]: {scan.intensities[i]:.2f}")

if __name__ == '__main__':
    rospy.init_node('lidar_subscriber')
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    rospy.spin()