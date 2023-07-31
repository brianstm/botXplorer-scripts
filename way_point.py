#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from geometry_msgs.msg import Twist
import time


def move_and_pose(point_num):
    # Move to point
    rospy.loginfo("Moving to point %d", point_num)
    move_base_pub.publish(get_move_goal(point_num))

    # Wait until finished moving
    rospy.loginfo("Waiting for robot to reach point %d", point_num)
    while not is_robot_stopped():
        rospy.sleep(1)

    # Delay before posing
    rospy.loginfo("Waiting for 2 seconds before posing")
    time.sleep(2)

    # Pose at the same point
    rospy.loginfo("Posing at point %d", point_num)
    initial_pose_pub.publish(get_initial_pose(point_num))

    rospy.sleep(1)


def get_move_goal(point_num):
    if point_num == 1:
        move_goal = PoseStamped()
        move_goal.header.frame_id = "map"
        move_goal.pose.position.x = 7.524
        move_goal.pose.position.y = -5.150
        move_goal.pose.orientation.z = -0.104
        move_goal.pose.orientation.w = 0.995
        return move_goal
    elif point_num == 2:
        move_goal = PoseStamped()
        move_goal.header.frame_id = "map"
        move_goal.pose.position.x = 0.724
        move_goal.pose.position.y = 7.123
        move_goal.pose.orientation.z = 0.728
        move_goal.pose.orientation.w = 0.686
        return move_goal
    else:
        return None


def get_initial_pose(point_num):
    if point_num == 1 or point_num == 2:
        initial_pose = PoseWithCovarianceStamped()
        initial_pose.header.frame_id = "map"
        initial_pose.pose.pose = get_move_goal(point_num).pose
        initial_pose.pose.covariance = [
            0.1, 0, 0, 0, 0, 0,
            0, 0.1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0
        ]
        return initial_pose
    else:
        return None


def is_robot_stopped():
    # Check if the robot is stopped by checking /cmd_vel values
    cmd_vel = rospy.wait_for_message('/cmd_vel', Twist)
    linear = cmd_vel.linear
    angular = cmd_vel.angular

    return linear.x == 0.0 and linear.y == 0.0 and linear.z == 0.0 and \
        angular.x == 0.0 and angular.y == 0.0 and angular.z == 0.0


if __name__ == '__main__':
    rospy.init_node('move_and_pose_script')

    move_base_pub = rospy.Publisher(
        '/move_base_simple/goal', PoseStamped, queue_size=1)
    initial_pose_pub = rospy.Publisher(
        '/initialpose', PoseWithCovarianceStamped, queue_size=1)

    # Prompt user for the number of times to repeat the sequence
    num_repeats = int(
        input("Enter the number of times to repeat the sequence (1-10): "))

    # Perform the sequence of movements and poses
    for i in range(num_repeats):
        move_and_pose(1)
        move_and_pose(2)

    # Move to the home position
    rospy.loginfo("Moving to home position")
    move_base_pub.publish(get_move_goal(0))

    # Wait until finished moving
    rospy.loginfo("Waiting for robot to reach home position")
    while not is_robot_stopped():
        rospy.sleep(1)

    # Pose at the home position
    rospy.loginfo("Posing at home position")
    initial_pose_pub.publish(get_initial_pose(0))

    rospy.spin()
