import rospy
import subprocess
import requests
import time
from datetime import datetime, timedelta


def time_sync():
    response = requests.get(
        "http://worldtimeapi.org/api/timezone/Asia/Singapore")
    if response.status_code == 200:
        api_data = response.json()
        datetime_str = api_data["datetime"]
        datetime_obj = datetime.fromisoformat(datetime_str)

        current_time = subprocess.check_output(['date']).decode().strip()
        rospy.loginfo("Current system time: %s", current_time)

        datetime_obj += timedelta(seconds=1)
        desired_time = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

        subprocess.call(
            'echo ubuntu | sudo -S date -s "{}"'.format(desired_time), shell=True)

        rospy.loginfo("System time set to: %s", desired_time)
    else:
        rospy.logerr("Failed to retrieve time from the API.")


if __name__ == '__main__':
    rospy.init_node('time_sync_node')

    try:
        time_sync()

        for _ in range(5):
            current_time = subprocess.check_output(['date']).decode().strip()
            rospy.loginfo("Current system time: %s", current_time)
            time.sleep(0.5)

    except KeyboardInterrupt:
        rospy.loginfo("Time synchronization interrupted by user.")
    except subprocess.CalledProcessError as e:
        rospy.logerr("Failed to set system time: %s", e.output.decode())

    rospy.loginfo("Exiting time_sync_node.")
