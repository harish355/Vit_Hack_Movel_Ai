#!/usr/bin/env python

import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import cv2
def main():

    rospy.init_node('send_goal_python')

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    rospy.loginfo('Waiting for the action server to start')
    client.wait_for_server()

    rospy.loginfo('Action server started, sending the goal')
    goal = MoveBaseGoal()
    goal.target_pose.header.stamp = rospy.Time.now()

    # set frame
    goal.target_pose.header.frame_id = 'map'

    # set position
    goal.target_pose.pose.position.x = -6.193
    goal.target_pose.pose.position.y = 4.23
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = -0.701
    goal.target_pose.pose.orientation.w = 0.712

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result')
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded')
    else:
        rospy.loginfo('Failed')

if __name__ == '__main__':
    img=cv2.imread("/home/mrstark/vithack/submap/room2.png")
    cv2.imshow("room2",img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    main()