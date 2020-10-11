

#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def handle_move():
    global z
    global a
    rospy.init_node('turtle_revolve' ,anonymous=True)
    pub = rospy.Publisher('/cmd_vel',Twist, queue_size = 10)
    speed=0
    rate=rospy.Rate(10)
    vel_msg = Twist()   
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)
    from evdev import InputDevice, categorize, ecodes
    gamepad = InputDevice('/dev/input/event5')
    print(gamepad)

    #evdev takes care of polling the controller in a loop
    for event in gamepad.read_loop():
        #print("speed : ",speed)
        #filters by event type
        if event.type == ecodes.EV_KEY:
            print(event)
            gh=str(event)
            a=gh.split()
            if a[4]=="304," and a[8]=="01":
                print("up")
                vel_msg.linear.x = speed
                vel_msg.angular.z = 0
                pub.publish(vel_msg)
            if a[4]=="306," and a[8]=="01":
                print("down")
                vel_msg.linear.x = -speed
                vel_msg.angular.z = 0
                pub.publish(vel_msg)
            if a[4]=="305," and a[8]=="01":
                print("right")
                vel_msg.linear.x = 0
                vel_msg.angular.z =-speed
                pub.publish(vel_msg)
            if a[4]=="307," and a[8]=="01":
                print("left")
                vel_msg.linear.x = 0
                vel_msg.angular.z = speed
                pub.publish(vel_msg)
            if a[4]=="310," and a[8]=="01":
                print("stop")
                vel_msg.linear.x = 0
                vel_msg.angular.z = 0
                pub.publish(vel_msg)
            if a[4]=="309," and a[8]=="01":
                print("speed ++")
                speed=speed+0.1
            if a[4]=="311," and a[8]=="01":
                print("speed --")
                if speed>0:
                    speed=speed-0.1
            if a[4]=="308," and a[8]=="01":
                break
    sys.exit(0)
           
if __name__ == "__main__":
    handle_move()