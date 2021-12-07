#! /usr/bin/env python3

import rospy
import math
from std_msgs.msg import Float64

def stand_straight():
    rospy.init_node('Stand',anonymous=False)
    f_left_top = rospy.Publisher('/trial3_assembly/fltj_position_controller/command', Float64, queue_size=10)
    f_right_top = rospy.Publisher('/trial3_assembly/frtj_position_controller/command', Float64, queue_size=10)
    b_left_top = rospy.Publisher('/trial3_assembly/bltj_position_controller/command', Float64, queue_size=10)
    b_right_top = rospy.Publisher('/trial3_assembly/brtj_position_controller/command', Float64, queue_size=10)
    f_left_knee = rospy.Publisher('/trial3_assembly/flkj_position_controller/command', Float64, queue_size=10)
    f_right_knee = rospy.Publisher('/trial3_assembly/frkj_position_controller/command', Float64, queue_size=10)
    b_left_knee = rospy.Publisher('/trial3_assembly/blkj_position_controller/command', Float64, queue_size=10)
    b_right_knee = rospy.Publisher('/trial3_assembly/brkj_position_controller/command', Float64, queue_size=10)
    sampling = 100
    bend_back_angle = math.pi/10
    fk_lift_angle = math.pi/6
    fh_lift_angle = math.pi/9
    zero = 0
    j=0
    while(j<bend_back_angle):
        f_left_top.publish(zero)
        f_right_top.publish(-zero)
        b_left_top.publish(-zero)
        b_right_top.publish(-zero)
        f_right_knee.publish(-zero)
        b_left_knee.publish(-zero)
        f_left_knee.publish(-j)
        b_right_knee.publish(-j)
        j=j+bend_back_angle/sampling
        rospy.sleep(0.1)
    j=0
    while(j<fh_lift_angle):
        b_left_knee.publish(-zero)
        b_right_knee.publish(-bend_back_angle)
        f_left_knee.publish(-bend_back_angle)
        f_left_top.publish(-j)
        f_right_top.publish(-zero)
        b_left_top.publish(-zero)
        b_right_top.publish(-j)
        f_right_knee.publish(-zero)
        j=j+fh_lift_angle/sampling
        rospy.sleep(0.1)
    j=0
    k=0
    while(j<bend_back_angle):
        b_left_knee.publish(-j)
        b_right_knee.publish(-bend_back_angle+j)
        f_left_knee.publish(-bend_back_angle+j)
        f_left_top.publish(-fh_lift_angle+k)
        f_right_top.publish(-zero)
        b_left_top.publish(-zero)
        b_right_top.publish(-fh_lift_angle+k)
        f_right_knee.publish(-j)
        j=j+bend_back_angle/sampling
        k=k+fh_lift_angle/sampling
        rospy.sleep(0.1)
    # j=0
    # k=0
    # while(j<fh_lift_angle):
    #     b_left_knee.publish(-bend_back_angle)
    #     b_right_knee.publish(-bend_back_angle+j)
    #     f_left_knee.publish(-bend_back_angle+j)
    #     f_left_top.publish(-fh_lift_angle+k)
    #     f_right_top.publish(-zero)
    #     b_left_top.publish(-zero)
    #     b_right_top.publish(-fh_lift_angle+k)
    #     f_right_knee.publish(-k)
    #     j=j+bend_back_angle/sampling
    #     k=k+fh_lift_angle/sampling
    #     rospy.sleep(0.1)
    
    
if __name__ == '__main__':
    try:
        stand_straight()
    except rospy.ROSInterruptException:
        pass