#! /usr/bin/env python3
import rospy
import math
from std_msgs.msg import Float64
from scipy.optimize import fsolve

def validate():
    #Sinusoidal movement of front right leg
    rospy.init_node('Inv_Validate',anonymous=False)
    f_left_top = rospy.Publisher('/trial5_assembly/fltj_position_controller/command', Float64, queue_size=10)
    f_right_top = rospy.Publisher('/trial5_assembly/frtj_position_controller/command', Float64, queue_size=10)
    b_left_top = rospy.Publisher('/trial5_assembly/bltj_position_controller/command', Float64, queue_size=10)
    b_right_top = rospy.Publisher('/trial5_assembly/brtj_position_controller/command', Float64, queue_size=10)
    f_left_knee = rospy.Publisher('/trial5_assembly/flkj_position_controller/command', Float64, queue_size=10)
    f_right_knee = rospy.Publisher('/trial5_assembly/frkj_position_controller/command', Float64, queue_size=10)
    b_left_knee = rospy.Publisher('/trial5_assembly/blkj_position_controller/command', Float64, queue_size=10)
    b_right_knee = rospy.Publisher('/trial5_assembly/brkj_position_controller/command', Float64, queue_size=10)
    flw_velocity = rospy.Publisher('/trial5_assembly/flwj_velocity_controller/command', Float64, queue_size=10)
    frw_velocity = rospy.Publisher('/trial5_assembly/frwj_velocity_controller/command', Float64, queue_size=10)
    blw_velocity = rospy.Publisher('/trial5_assembly/blwj_velocity_controller/command', Float64, queue_size=10)
    brw_velocity = rospy.Publisher('/trial5_assembly/brwj_velocity_controller/command', Float64, queue_size=10)
    
    #initial pose of the bot

    flka=0
    frka=0
    blka=0
    brka=0
    flha=0.3
    frha=0.3
    blha=0.3
    brha=0.3

    #leg lengths

    k = 380
    h = 356

    #initial coordinates of end effector with respect to hip joint

    samp = 0.001
    loop = math.radians(0)
    x = -k * math.cos(math.radians(65) - 0.3) + h * math.cos(-0.3)
    y = -k * math.sin(math.radians(65) - 0.3) + h * math.sin(-0.3)
    # print("Initial x and y",x,y)
    #print(initial_x,initial_y)
    while not rospy.is_shutdown():
        samp = 0.001
        loop = math.radians(0)
        x = -k * math.cos(math.radians(65) - 0.3) + h * math.cos(-0.3)
        y = -k * math.sin(math.radians(65) - 0.3) + h * math.sin(-0.3)
        f_left_knee.publish(-flka)
        f_right_knee.publish(frka)
        b_left_knee.publish(-blka)
        b_right_knee.publish(-brka)
        f_left_top.publish(-flha)
        f_right_top.publish(frha)
        b_left_top.publish(-blha)
        b_right_top.publish(-brha)
        flw_velocity.publish(0)
        frw_velocity.publish(0)
        blw_velocity.publish(0)
        brw_velocity.publish(0)
        loop = math.radians(0)
        while(loop<math.radians(90)):
            x = x-samp*50
            y = y+(0.1*math.sin(loop))
            print("X,Y: ",x,y)
            th2 = math.acos((math.pow(k, 2) + math.pow(h, 2) - math.pow(x, 2) - math.pow(y, 2)) / (2 * k * h))
            frka = th2 - math.radians(65)
            print("theta2: ",math.degrees(th2))
            a = -k*math.cos(th2)+h
            b = k*math.sin(th2)
            th1 = math.atan2(b,a) + math.atan2(y,x)
            frha = th1
            print("theta1: ",math.degrees(th1))
            rospy.sleep(0.01)
            loop+=0.001
            f_left_knee.publish(-flka)
            f_right_knee.publish(frka)
            b_left_knee.publish(-blka)
            b_right_knee.publish(-brka)
            f_left_top.publish(-flha)
            f_right_top.publish(frha)
            b_left_top.publish(-blha)
            b_right_top.publish(-brha)
            flw_velocity.publish(0)
            frw_velocity.publish(0)
            blw_velocity.publish(0)
            brw_velocity.publish(0)
        loop = math.radians(90)
        while(loop<math.radians(180)):
            x = x-samp*50
            y = y-(0.1*math.sin(loop))
            print("X,Y: ",x,y)
            th2 = math.acos((math.pow(k, 2) + math.pow(h, 2) - math.pow(x, 2) - math.pow(y, 2)) / (2 * k * h))
            frka = th2 - math.radians(65)
            print("theta2: ",math.degrees(th2))
            a = -k * math.cos(th2) + h
            b = k * math.sin(th2)
            frha = th1
            th1 = math.atan2(b,a) + math.atan2(y,x)
            print("theta1: ", math.degrees(th1))
            rospy.sleep(0.01)
            loop+=0.001
            f_left_knee.publish(-flka)
            f_right_knee.publish(frka)
            b_left_knee.publish(-blka)
            b_right_knee.publish(-brka)
            f_left_top.publish(-flha)
            f_right_top.publish(frha)
            b_left_top.publish(-blha)
            b_right_top.publish(-brha)
            flw_velocity.publish(0)
            frw_velocity.publish(0)
            blw_velocity.publish(0)
            brw_velocity.publish(0)
        while(frha<-0.3):
            frha = frha + 0.001
            f_left_knee.publish(-flka)
            f_right_knee.publish(frka)
            b_left_knee.publish(-blka)
            b_right_knee.publish(-brka)
            f_left_top.publish(-flha)
            f_right_top.publish(frha)
            b_left_top.publish(-blha)
            b_right_top.publish(-brha)
            flw_velocity.publish(0)
            frw_velocity.publish(0)
            blw_velocity.publish(0)
            brw_velocity.publish(0)
            rospy.sleep(0.01)

if __name__ == '__main__':
    try:
        validate()
    except rospy.ROSInterruptException:
        pass