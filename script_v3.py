#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class MagniController:
    def __init__(self):
        print('Starting MagniController...')
        rospy.init_node('magni_controller')
        rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.twist = Twist()
        self.twist.linear.x = 0.2 # Set the initial speed of the Magni Bot to 0.2 m/s
        self.distance_field_1 = 0.1 # Set the minimum distance for field 1 (10 cm)
        self.distance_field_2 = 0.5 # Set the minimum distance for field 2 (50 cm)

    def laser_callback(self, scan):
        field_1 = scan.ranges[0:60] # Get the laser scan data for field 1 (0-60 degrees)
        field_2 = scan.ranges[300:359] # Get the laser scan data for field 2 (300-359 degrees)
        distance_1 = min(field_1) # Find the minimum distance in field 1
        distance_2 = min(field_2) # Find the minimum distance in field 2

        print('distance_1:', distance_1)
        print('distance_2:', distance_2)

        if distance_1 < self.distance_field_1:
            # Stop the Magni Bot if an object is detected in field 1
            print('Stopping...')
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.0
            self.pub.publish(self.twist)
        elif distance_2 < self.distance_field_2:
            # Slow down the Magni Bot if an object is detected in field 2
            print('Slowing down...')
            self.twist.linear.x = 0.1
            self.twist.angular.z = 0.0
            self.pub.publish(self.twist)
        else:
            # Continue moving forward if no objects are detected
            print('Moving forward...')
            self.twist.linear.x = 0.2
            self.twist.angular.z = 0.0
            self.pub.publish(self.twist)

if __name__ == '__main__':
    try:
        controller = MagniController()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
