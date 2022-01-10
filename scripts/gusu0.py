#!/usr/bin/env python3

"""
BSD 2-Clause "Simplified" License
Copyright (c) 2022 Ryuichi Ueda & Yuma Ito.
All rights reserved.
"""

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data
    
rospy.init_node('gusu0')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('gusu0', Int32, queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    if n % 2 == 0:
        n = 0;
    pub.publish(n)
    rate.sleep()
