#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
import subprocess


class ObstacleAvoider:
    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.pose_pub = rospy.Publisher(
            '/initialpose', PoseWithCovarianceStamped, queue_size=1)
        self.lidar_sub = rospy.Subscriber(
            '/scan', LaserScan, self.lidar_callback)
        self.cmd_vel_sub = rospy.Subscriber(
            '/cmd_vel', Twist, self.cmd_vel_callback)
        self.process = subprocess.Popen(
            ["roslaunch", "magni_navigation1", "move_base.launch"])
        self.lastest_cmd_vel_point = Twist()

    def lidar_callback(self, data):
        lidar_output_state = data.ranges
        if lidar_output_state[-1] == 1 and self.process.poll() is not None:
            self.process = subprocess.Popen(
                ["roslaunch", "magni_navigation1", "move_base.launch"])
            pose = PoseWithCovarianceStamped()
            pose.pose.pose.position.x = self.lastest_cmd_vel_point.linear.x
            pose.pose.pose.position.y = self.lastest_cmd_vel_point.linear.y
            pose.pose.pose.orientation.z = self.lastest_cmd_vel_point.linear.z
            self.pose_pub.publish(pose)
        elif lidar_output_state[-1] == 0 and self.process.poll() is None:
            self.process.terminate()

    def cmd_vel_callback(self, data):
        self.lastest_cmd_vel_point = data


if __name__ == '__main__':
    rospy.init_node('obstacle_avoider')
    avoider = ObstacleAvoider()
    rospy.spin()
