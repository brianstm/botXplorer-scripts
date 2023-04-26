#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ObstacleAvoidance:
    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        self.twist = Twist()
        self.twist.linear.x = 0.2
        self.stop_distance = 0.1 
        self.slow_down_distance = 0.5
        self.distance_to_obstacle = float('inf') 
        self.start_time = rospy.get_time()
        self.drive_duration = 3.0
        self.is_obstacle_detected = False 

    def laser_callback(self, data):
        self.distance_to_obstacle = min(data.ranges)

        if self.distance_to_obstacle < self.stop_distance:
            self.twist.linear.x = 0.0 
            self.is_obstacle_detected = True 
            print('Obstacle detected! Stopping the robot...')
        elif self.distance_to_obstacle < self.slow_down_distance:
            self.twist.linear.x = 0.1 
            self.is_obstacle_detected = True 
            print('Obstacle detected! Slowing down the robot...')
        else:
            self.twist.linear.x = 0.2
            self.is_obstacle_detected = False 

    def drive(self):
        while not rospy.is_shutdown() and rospy.get_time() - self.start_time < self.drive_duration and not self.is_obstacle_detected:
            self.cmd_vel_pub.publish(self.twist)
            rospy.sleep(0.1)

        self.twist.linear.x = 0.0
        self.cmd_vel_pub.publish(self.twist)

if __name__ == '__main__':
    rospy.init_node('obstacle_avoidance')
    obstacle_avoidance = ObstacleAvoidance()
    obstacle_avoidance.drive()
