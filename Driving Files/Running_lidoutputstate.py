#!/usr/bin/env python

# This is the working one, it will move the robot and will slow down and stop when the
# field is detected in the SICK TiM781 LiDAR Sensor lidoutputstate.
import rospy
from sick_scan.msg import LIDoutputstateMsg
from geometry_msgs.msg import Twist


class ObstacleDetector:
    def __init__(self):
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.lidar_sub = rospy.Subscriber(
            '/sick_tim_7xx/lidoutputstate', LIDoutputstateMsg, self.lidar_callback)
        self.twist = Twist()
        self.obstacle_field1 = False
        self.obstacle_field2 = False
        self.last_obstacle_field1 = False

    def lidar_callback(self, data):
        lidar_output_state = data.output_state
        print("0:", data.output_state[0])
        print("1:", data.output_state[1])
        print("2:", data.output_state[2])
        print("3:", data.output_state[3])

        if (lidar_output_state[0] == 0):
            self.obstacle_field1 = True
        else:
            self.obstacle_field1 = False

        if (lidar_output_state[1] == 0):
            self.obstacle_field2 = True
        else:
            self.obstacle_field2 = False

    def drive(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if not self.obstacle_field1 and self.last_obstacle_field1:
                time_since_clear = rospy.get_time() - self.obstacle_field1_time
                if time_since_clear >= 5:
                    self.twist.linear.x = 0.7

            elif self.obstacle_field1:
                if not self.last_obstacle_field1:
                    self.obstacle_field1_time = rospy.get_time()

                self.twist.linear.x = 0
            elif self.obstacle_field2:
                self.twist.linear.x = 0.2
            else:
                self.twist.linear.x = 0.7

            self.cmd_pub.publish(self.twist)
            rate.sleep()
            self.last_obstacle_field1 = self.obstacle_field1


if __name__ == '__main__':
    rospy.init_node('obstacle_detector', anonymous=True)
    obstacle_detector = ObstacleDetector()
    obstacle_detector.drive()
