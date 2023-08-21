#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

class LidarTelemetry:
    def __init__(self):
        rospy.init_node('lidar_telemetry')
        rospy.Subscriber('/scan', LaserScan, self.laser_callback)

    def laser_callback(self, scan):
        distance_front = scan.ranges[len(scan.ranges)/2]
        print('Distance to obstacle in front:', distance_front)

if __name__ == '__main__':
    try:
        telemetry = LidarTelemetry()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
