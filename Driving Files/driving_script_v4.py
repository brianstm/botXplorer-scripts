#!/usr/bin/env python

import rospy
import time
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
        self.distance_field_1 = 0.3 # Set the minimum distance for field 1 (10 cm)
        self.distance_field_2 = 0.7 # Set the minimum distance for field 2 (50 cm)
        self.start_time = time.time() # Store the current time
        self.run_duration = 5.0 # Set the duration to run (in seconds)
        self.run_distance = 5.0 # Set the distance to run (in meters)
        self.total_distance = 0.0 # Keep track of the total distance traveled

    def laser_callback(self, scan):
        field_1 = scan.ranges[0:60] # Get the laser scan data for field 1 (0-60 degrees)
        field_2 = scan.ranges[300:359] # Get the laser scan data for field 2 (300-359 degrees)
        distance_1 = min(field_1) # Find the minimum distance in field 1
        distance_2 = min(field_2) # Find the minimum distance in field 2

        print('distance_1:', distance_1)
        print('distance_2:', distance_2)

        if time.time() - self.start_time > self.run_duration or self.total_distance > self.run_distance:
            # Stop the Magni Bot if the run duration or distance has been exceeded
            print('Stopping...')
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.0
            self.pub.publish(self.twist)
        elif distance_1 < self.distance_field_1:
            # Slow down the Magni Bot if an object is detected in field 1
            print('Slowing down...')
            self.twist.linear.x = 0.1
            self.twist.angular.z = 0.0
            self.pub.publish(self.twist)
        elif distance_2 < self.distance_field_2:
            # Slow down the Magni Bot if an object is detected in field 2
            print('Slowing down...')
            self.twist.linear.x = 0.1
            self.twist.angular.z = 0.0
            self.pub.publish(self.twist)
        else:
            # Move forward if no objects are detected
            print('Moving forward...')
            self.twist.linear.x = 0.2
            self.twist.angular.z = 0.0
            self.pub.publish(self.twist)
            self.total_distance += self.twist.linear.x * (time.time() - self.start_time) # Update the total distance traveled

if __name__ == '__main__':
    try:
        controller = MagniController()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
