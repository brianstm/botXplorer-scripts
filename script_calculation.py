#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(data):
    ranges = [round(distance, 2) for distance in data.ranges] 

    slowing_down = False
    stopping = False
    for distance in ranges:
        if distance <= 0.4:
            slowing_down = True
        if distance <= 0.2:
            stopping = True

    if stopping:
        print("STOPPING")
    elif slowing_down:
        print("SLOWING DOWN")
    else:
        print("RUNNING")

if __name__ == '__main__':
    rospy.init_node('lidar_subscriber')
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    rospy.spin()
