#!/usr/bin/env python

import sys
sys.path.append('/usr/lib/python3/dist-packages/')

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

class MagniBot:
    def __init__(self):
        rospy.init_node('magni_bot', anonymous=True)
        self.lidar_sub = rospy.Subscriber("/scan", LaserScan, self.lidar_callback)
        self.velocity_pub = rospy.Publisher('/cmd_vel', String, queue_size=10)
        self.obstacle_detected = False
        self.field_set_complete = False
        self.distance_traveled = 0
        self.max_distance = 3 # in meters
        
    def lidar_callback(self, data):
        # get the distance to the closest obstacle in front of the robot
        min_distance = min(data.ranges)
        if min_distance < 0.5: # if an obstacle is detected
            self.obstacle_detected = True
        elif min_distance > 2 and self.field_set_complete: # if the robot has finished the field set
            self.obstacle_detected = True
        
    def run(self):
        # set the robot's speed and direction
        self.velocity_pub.publish('forward 0.2')
        while not self.obstacle_detected and self.distance_traveled < self.max_distance:
            rospy.sleep(0.1) # wait for the lidar data to update
            self.distance_traveled += 0.2 # update the distance traveled
        self.velocity_pub.publish('stop')
        
        if self.obstacle_detected:
            print("Obstacle detected! Stopping the robot.")
        else:
            print("Field set completed successfully!")
            self.field_set_complete = True
            
            # wait for the robot to stop moving
            rospy.sleep(1)
            
            # turn the robot around and head back to the start
            self.velocity_pub.publish('rotate -1.5')
            rospy.sleep(3.5) # turn for 3.5 seconds
            self.velocity_pub.publish('stop')
            
            # wait for the robot to stop moving
            rospy.sleep(1)
            
            # drive back to the start
            self.velocity_pub.publish('forward 0.2')
            rospy.sleep(15) # drive for 15 seconds
            self.velocity_pub.publish('stop')
            
if __name__ == '__main__':
    try:
        magni_bot = MagniBot()
        magni_bot.run()
    except rospy.ROSInterruptException:
        pass
