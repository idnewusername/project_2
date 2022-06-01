#!/usr/bin/env python
import rospy 
import time
from std_msgs.msg import Float32 
from geometry_msgs.msg import Twist 

angle = rospy.Publisher("/angle_flippers", Float32, queue_size=10)

move = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

param = [0, "forward_1", "angle_1"]
move_cmd = Twist()

def start():

    rospy.init_node('control_flippers')
    while not rospy.is_shutdown():

         if param[2] == "angle_1":
            if param[0] > (-0.6):
               param[0]+=(-0.02)

            if param[0] < (-0.6):
                  param[2] = "angle_0"

         elif param[2] == "angle_0":
              rospy.sleep(0.7)
              move_f_1()


         elif param[2] == "angle_2":
            if param[0] < (0.25):
               param[0]+=(0.015)

            if param[0] > (0.25):
               param[2] = "angle_0"
               param[1] = "forward_3"
               param[2] = "angle_3"


         elif param[2] == "angle_3":
            if param[0] < (1.23):
               param[0]+=(0.03)

            if param[0] > (1.23):
               param[2] = "angle_0"


         elif param[2] == "angle_4":
            if param[0] > (0):
               param[0]+=(-0.03)

            if param[0] < (0):
               param[1] = "forward_0"
               move_f_1()


         rospy.Rate(40).sleep()
         angle.publish(param[0])


def move_f_1():

   if param[1] == "forward_1":
         end = True
         move_cmd.linear.x = 0.2
         target_time = rospy.Time.now() + rospy.Duration.from_sec(3.5)
         if end == True:
            while rospy.Time.now() < target_time:
                     move.publish(move_cmd)
            else:
                     end = False
                     param[1] = "forward_2"

         if end == False:
                  param[2] = "angle_2"


   if param[1] == "forward_2":
        move_cmd.linear.x = 0.1
        move.publish(move_cmd)


   if param[1] == "forward_3":

        move_cmd.linear.x = 0.015
        check = True
        target_time_1 = rospy.Time.now() + rospy.Duration.from_sec(3.5)

        if check == True:
           while rospy.Time.now() < target_time_1:
                    move.publish(move_cmd)
           else:
                    check = False
                    param[1] = "forward_4"

        if check == False:
                 param[2] = "angle_4"

   if param[1] == "forward_4":
        move_cmd.linear.x = 0.9
        move.publish(move_cmd)


   if param[1] == "forward_0":
        move_cmd.linear.x = 0
        move.publish(move_cmd)


if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
