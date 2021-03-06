#! /usr/bin/env python3

import rospy
import math
from rospy.core import is_shutdown
from std_msgs.msg import Float64
import sys, select, termios, tty

msg = "\tIMPORTANT: CONTROL YOUR BOT USING THE KEYS WASD and SPACE\n spacebar: stop the vehicle abruptly\n longpress w: increase the forward velocity\n longpress d: decrease the velocity and move backward\n longpress a: move to the left \n longpress s: move to the right\n"
print(msg)
"""
Moving Around:
--------------------
        w
    a       s
        d

    Space Bar
    
spacebar: stop the vehicle abruptly
longpress w: increase the forward velocity
longpress d: decrease the velocity and move backward
longpress a: move to the left 
longpress s: move to the right

"""


def getKey():
    settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def stand_straight():
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('Stand',anonymous=False)
    f_left_top = rospy.Publisher('/trial6_assembly/fltj_position_controller/command', Float64, queue_size=10)
    f_right_top = rospy.Publisher('/trial6_assembly/frtj_position_controller/command', Float64, queue_size=10)
    b_left_top = rospy.Publisher('/trial6_assembly/bltj_position_controller/command', Float64, queue_size=10)
    b_right_top = rospy.Publisher('/trial6_assembly/brtj_position_controller/command', Float64, queue_size=10)
    f_left_knee = rospy.Publisher('/trial6_assembly/flkj_position_controller/command', Float64, queue_size=10)
    f_right_knee = rospy.Publisher('/trial6_assembly/frkj_position_controller/command', Float64, queue_size=10)
    b_left_knee = rospy.Publisher('/trial6_assembly/blkj_position_controller/command', Float64, queue_size=10)
    b_right_knee = rospy.Publisher('/trial6_assembly/brkj_position_controller/command', Float64, queue_size=10)
    flw_velocity = rospy.Publisher('/trial6_assembly/flwj_velocity_controller/command', Float64, queue_size=10)
    frw_velocity = rospy.Publisher('/trial6_assembly/frwj_velocity_controller/command', Float64, queue_size=10)
    blw_velocity = rospy.Publisher('/trial6_assembly/blwj_velocity_controller/command', Float64, queue_size=10)
    brw_velocity = rospy.Publisher('/trial6_assembly/brwj_velocity_controller/command', Float64, queue_size=10)
    m1j = rospy.Publisher('/trial6_assembly/m1j_position_controller/command', Float64, queue_size=10)
    m2j = rospy.Publisher('/trial6_assembly/m2j_position_controller/command', Float64, queue_size=10)
    m3j = rospy.Publisher('/trial6_assembly/m3j_position_controller/command', Float64, queue_size=10)
    m4j = rospy.Publisher('/trial6_assembly/gripperj_position_controller/command', Float64, queue_size=10)
    
    
    flka=0
    frka=0
    blka=0
    brka=0
    flha=0.3
    frha=0.3
    blha=0.3
    brha=0.3

    zero = 0
    
    velocity = 0
    l_diff_velocity = 0
    r_diff_velocity = 0
    max_velocity = 10
    max_diff_velocity = 3
    
    
    f_left_knee.publish(-flka)
    f_right_knee.publish(-frka)
    b_left_knee.publish(-blka)
    b_right_knee.publish(-brka)
    f_left_top.publish(-flha)
    f_right_top.publish(-frha)
    b_left_top.publish(-blha)
    b_right_top.publish(-brha)
    flw_velocity.publish(velocity)
    frw_velocity.publish(velocity)
    blw_velocity.publish(velocity)
    brw_velocity.publish(velocity)
    while not rospy.is_shutdown():
        key_pressed = getKey()
        if key_pressed == 'w':
            velocity += 0.25
        elif key_pressed =='s':
            velocity -= 0.25
        elif (key_pressed == 'a'):
            if(r_diff_velocity > 0.1):
                r_diff_velocity = r_diff_velocity - 0.2
            elif(r_diff_velocity < -0.1):
                r_diff_velocity += 0.2
            else:
                l_diff_velocity += 0.2
        elif (key_pressed == 'd'):
            if(l_diff_velocity > 0.1):
                l_diff_velocity = l_diff_velocity - 0.2
            elif(l_diff_velocity < -0.1):
                l_diff_velocity += 0.2
            else:
                r_diff_velocity += 0.2
        elif key_pressed == ' ':
            velocity = 0
            r_diff_velocity = 0
            l_diff_velocity = 0            
        elif key_pressed == 'z':
            brha -= 0.01
            blha -= 0.01
            brka += 0.01
            blka += 0.01
        elif key_pressed == 'q':
            brha += 0.01
            blha += 0.01
            brka -= 0.01
            blka -= 0.01
        elif key_pressed == 'c':
            frha -= 0.01
            flha -= 0.01
            frka += 0.01
            flka += 0.01
        elif key_pressed == 'e':
            frha += 0.01
            flha += 0.01
            frka -= 0.01
            flka -= 0.01
        elif key_pressed == '1':
            flka += 0.01
        elif key_pressed =='2':
            flka -= 0.01
        elif key_pressed =='3':
            frka += 0.01
        elif key_pressed =='4':
            frka -= 0.01
        elif key_pressed =='5':
            blka += 0.01
        elif key_pressed =='6':
            blka -= 0.01
        elif key_pressed =='7':
            brka += 0.01
        elif key_pressed == '8':
            brka -= 0.01
        elif key_pressed == 'r':
            flha += 0.01
        elif key_pressed == 'f':
            flha -= 0.01
        elif key_pressed == 't':
            frka += 0.01
        elif key_pressed == 'g':
            frka -= 0.01
        elif key_pressed == 'y':
            blha += 0.01
        elif key_pressed == 'h':
            blha -= 0.01
        elif key_pressed == 'u':
            brha += 0.01
        elif key_pressed == 'j':
            brha -= 0.01
        if(velocity>=0):
            velocity = min(velocity,max_velocity)
        else:
            velocity = max(velocity,-(max_velocity))
        if(l_diff_velocity>=0):
            l_diff_velocity = min(l_diff_velocity,max_diff_velocity)
        else:
            l_diff_velocity  = max(l_diff_velocity,-(max_diff_velocity))
        if(r_diff_velocity>=0):
            r_diff_velocity = min(r_diff_velocity,max_diff_velocity)
        else:
            r_diff_velocity = max(r_diff_velocity,-(max_diff_velocity))
        
        print("Velocity: ",velocity, " left_diff_velocity: ",l_diff_velocity," right_diff_velocity: ",r_diff_velocity,"\n")
        f_left_knee.publish(-flka)
        f_right_knee.publish(-frka)
        b_left_knee.publish(-blka)
        b_right_knee.publish(-brka)
        f_left_top.publish(-flha)
        f_right_top.publish(-frha)
        b_left_top.publish(-blha)
        b_right_top.publish(-brha)
        m1j.publish(zero)
        m2j.publish(zero)
        m3j.publish(zero)
        m4j.publish(zero)
        if(velocity>=0):
            flw_velocity.publish(velocity-l_diff_velocity)
            frw_velocity.publish(velocity-r_diff_velocity)
            blw_velocity.publish(velocity-l_diff_velocity)
            brw_velocity.publish(velocity-r_diff_velocity)
        else:
            flw_velocity.publish(velocity+l_diff_velocity)
            frw_velocity.publish(velocity+r_diff_velocity)
            blw_velocity.publish(velocity+l_diff_velocity)
            brw_velocity.publish(velocity+r_diff_velocity)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
if __name__ == '__main__':
    try:
        stand_straight()
    except rospy.ROSInterruptException:
        pass