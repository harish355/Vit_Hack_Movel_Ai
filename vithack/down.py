
#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
z=0
def pose(pose):
    global z
    z=pose.theta

def handle_move_circle():
    global z
    global a
    rospy.init_node('turtle_revolve' ,anonymous=True)

    pub = rospy.Publisher('/cmd_vel',Twist, queue_size = 10)
    rate=rospy.Rate(10)
    vel_msg = Twist()   
    vel_msg.linear.x = -0.1
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)

    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        import time
        time.sleep(2)
        pub.publish(vel_msg)
        break
if __name__ == "__main__":
    handle_move_circle()