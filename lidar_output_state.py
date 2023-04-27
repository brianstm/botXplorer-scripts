#!/usr/bin/env python

# header:
#   seq: 814
#   stamp:
#     secs: 1682560878
#     nsecs: 365259740
#   frame_id: "sick_tim_7xx"
# version_number: 0
# system_counter: 1582256000
# output_state: [0, 0, 0, 1]
# output_count: [12, 774, 0, 4]
# time_state: 0
# year: 0
# month: 0
# day: 0
# hour: 0
# minute: 0
# second: 0
# microsecond: 0

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def scan_callback(data):
    field1Current = data.output_count[0]
    field2Current = data.output_count[1]

    if field1Current > field1Prev:
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = 0.0
        cmd_vel_pub.publish(twist_msg)

    if field2Current > field2Prev:
        twist_msg.linear.x = 0.5 
        twist_msg.angular.z = 0.0
        cmd_vel_pub.publish(twist_msg)

    field1Prev = field1Current
    field2Prev = field2Current

if __name__ == '__main__':
    rospy.init_node('lidar_subscriber')
    rospy.Subscriber("/sick_tim_7xx/lidoutputstate", LaserScan, scan_callback)

    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    twist_msg = Twist()
    twist_msg.linear.x = 0.0
    twist_msg.angular.z = 0.0

    field1Prev = 0
    field2Prev = 0

    rospy.spin()

