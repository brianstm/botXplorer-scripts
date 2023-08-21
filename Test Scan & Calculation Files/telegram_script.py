#!/usr/bin/env python

import rospy
from sick_scan.msg import SickScanTelegramMsg

def telegram_callback(msg):
    telegram = msg.telegram
    print('Received Telegram: {}'.format(telegram))

if __name__ == '__main__':
    rospy.init_node('telegram_subscriber')
    rospy.Subscriber('/sick_scan/telegram', SickScanTelegramMsg, telegram_callback)
    rospy.spin()
