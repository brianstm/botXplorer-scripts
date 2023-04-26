import rospy
from sensor_msgs.msg import LaserScan
import math # install python math

def callback(data):
    angle_min = math.degrees(data.angle_min)
    angle_max = math.degrees(data.angle_max)
    angle_increment = math.degrees(data.angle_increment)
    time_increment = data.time_increment
    scan_time = data.scan_time
    range_min = data.range_min
    range_max = data.range_max
    ranges = [round(distance, 2) for distance in data.ranges] 
    intensities = data.intensities

    print("angle_min:", angle_min)
    print("angle_max:", angle_max)
    print("angle_increment:", angle_increment)
    print("time_increment:", time_increment)
    print("scan_time:", scan_time)
    print("range_min:", range_min)
    print("range_max:", range_max)
    print("ranges (m):", ranges)
    print("intensities:", intensities)
    print("")

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
