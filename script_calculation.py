#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(data):
    ranges = [round(distance, 2) for distance in data.ranges]
    print("-----")
    print(len(ranges))
    for i in ranges:
        print(i) 


if __name__ == '__main__':
    rospy.init_node('lidar_subscriber')
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    rospy.spin()
