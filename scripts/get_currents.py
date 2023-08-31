#!/usr/bin/env python

from __future__ import print_function
import rospy
from sensor_msgs.msg import JointState
import csv

currents = []

def callback(data): 
    print(data.effort[0])
    currents.append(data.effort[0])

def get_data():
    rospy.init_node("current_record")
    rospy.Subscriber("joint_states", JointState, callback)

    rospy.spin()


if __name__ == '__main__':

    try:
        get_data()
    except rospy.ROSInterruptException:
        pass

    print(f"min {min(currents)}")