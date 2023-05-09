
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range

OBSTACLE_DIST = 0.2

class UbiquityBot(object):

    def __init__(self):
        rospy.init_node('ubquity_controller_sonars')

        self.sonar_sub = rospy.Subscriber('/sonars', Range, self.sonar_callback)

        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        self.twist_msg = Twist()
        self.twist_msg.linear.x = 0.2

        self.loop()

    def sonar_callback(self, msg):
        if msg.range < OBSTACLE_DIST:
            self.twist_msg.linear.x = 0
            self.cmd_vel_pub.publish(self.twist_msg)

    def loop(self):
        rate = rospy.Rate(10) 
        while not rospy.is_shutdown():
            self.cmd_vel_pub.publish(self.twist_msg)
            rate.sleep()

if __name__ == '__main__':
    try:
        UbiquityBot()
    except rospy.ROSInterruptException:
        pass
