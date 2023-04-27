#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(data):
    ranges = [round(distance, 2) for distance in data.ranges] 
    
    max_range = max(ranges)
    print("Max Range: ", max_range)

    if max_range <= 0.4:
        print("SLOWING DOWN")
    elif max_range <= 0.2:
        print("STOPPING")
    else:
        print("RUNNING")

if __name__ == '__main__':
    rospy.init_node('lidar_subscriber')
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    rospy.spin()
