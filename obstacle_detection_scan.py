#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

class AvoidanceNode:
    def __init__(self):
        rospy.init_node('collision_avoidance_node')
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        self.threshold_distance = 1.0
        
    def laser_callback(self, msg):
        front_sector = msg.ranges[270:270] 
        closest = min(front_sector)
        
        if closest < self.threshold_distance:
            rospy.loginfo('Obstacle detected {} meters ahead'.format(closest))
            # Insert your robot's action here or publish to an action topic to make the robot move/stop, etc
        
if __name__ == '__main__':
    node = AvoidanceNode()
    rospy.spin()
