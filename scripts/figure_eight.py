#!/usr/bin/env python

# Motor current testing script

from __future__ import print_function
import rospy
from math import cos, pi, sin, sqrt
from geometry_msgs.msg import Twist

def figure_eight():
    pub = rospy.Publisher('/cmd_vel',Twist, queue_size=10) 
    rate = rospy.Rate(10)

    t = 0.0                 
    a = 2.5
    count = 0

    T = rospy.get_param('~T', 20) 

    path = Twist()  

    while not rospy.is_shutdown():
        xdot = a*cos(4.0*pi*t/T)*4.0*pi/T
        ydot = a*cos(2.0*pi*t/T)*2.0*pi/T

        xdotdot = -a*sin(4*pi*t/T)*(4.0*pi/T)**2
        ydotdot = -a*sin(2*pi*t/T)*(2.0*pi/T)**2

        v = sqrt(xdot**2+ydot**2)
        w = (ydotdot*xdot - xdotdot*ydot) / (xdot**2 + ydot**2)

        path.linear.x = v
        path.angular.z = w
        pub.publish(path)

        # increment time
        if t == T:
            t = 0.0
        else:
            t = t + 0.1
            
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('figure_eight_node')
    try:
        figure_eight()
    except rospy.ROSInterruptException:
        pass


