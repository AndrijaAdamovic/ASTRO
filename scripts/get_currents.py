#!/usr/bin/env python

from __future__ import print_function
import rospy
from sensor_msgs.msg import JointState
import csv

currents = []

def callback(data):     
    current = abs(data.effort[1])
    print(current)
    currents.append(current)

def get_data():
    rospy.init_node("current_record")
    rospy.Subscriber("joint_states", JointState, callback)

    rospy.spin()


if __name__ == '__main__':

    try:
        get_data()
    except rospy.ROSInterruptException:
        pass

    print(f"max {max(currents)}")