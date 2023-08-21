#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from sick_tim.msg import SickScan

def lidar_callback(data):
    # Convert SickScan data to LaserScan data
    scan = LaserScan()
    scan.header = data.header
    scan.angle_min = data.angle_min
    scan.angle_max = data.angle_max
    scan.angle_increment = data.angle_increment
    scan.time_increment = data.time_increment
    scan.scan_time = data.scan_time
    scan.range_min = data.range_min
    scan.range_max = data.range_max
    scan.ranges = list(data.ranges)
    scan.intensities = list(data.intensities)

    # Publish the LaserScan data on the /scan topic
    scan_pub.publish(scan)

if __name__ == '__main__':
    rospy.init_node('lidar_node')
    scan_pub = rospy.Publisher('/scan', LaserScan, queue_size=10)
    rospy.Subscriber('/scan_raw', SickScan, lidar_callback)
    rospy.spin()