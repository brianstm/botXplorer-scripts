#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(data):
    # for i, r in enumerate(scan.ranges):
    #     print(f"Range[{i}]: {r:.2f}  Intensity[{i}]: {scan.intensities[i]:.2f}")
    angle_min = math.degrees(data.angle_min)
    angle_max = math.degrees(data.angle_max)
    angle_increment = math.degrees(data.angle_increment)
    time_increment = data.time_increment
    scan_time = data.scan_time
    range_min = data.range_min
    range_max = data.range_max
    ranges = [round(distance, 2) for distance in data.ranges] 
    intensities = data.intensities

    print("angle_min:", angle_min)
    print("angle_max:", angle_max)
    print("angle_increment:", angle_increment)
    print("time_increment:", time_increment)
    print("scan_time:", scan_time)
    print("range_min:", range_min)
    print("range_max:", range_max)
    print("ranges (m):", ranges)
    print("intensities:", intensities)
    print("")

if __name__ == '__main__':
    rospy.init_node('lidar_subscriber')
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    rospy.spin()