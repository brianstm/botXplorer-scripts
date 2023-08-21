#!/usr/bin/env python

import rospy
from sick_scan.msg import LIDoutputstateMsg

def scan_callback(data):
    state = data.output_count

    field1 = state[0]
    field2 = state[1]

    print("field1:", field1)
    print("field2:", field2)
    print("---------------------------------")

if __name__ == '__main__':
    rospy.init_node('lidar_subscriber')
    rospy.Subscriber("/sick_tim_7xx/lidoutputstate", LIDoutputstateMsg, scan_callback)
    rospy.spin()
