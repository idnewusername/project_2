#!/usr/bin/env python
import rospy 
import time
from std_msgs.msg import Float32 
from geometry_msgs.msg import Twist 

angle = rospy.Publisher("/angle_flippers", Float32, queue_size=10)

move = rospy.Publisher("/simple_tracked/cmd_vel_twist", Twist, queue_size=10)

param = [0, "forward_1", "angle_1"]
move_cmd = Twist()

def start():

    nachalo = True
    rospy.init_node('control_flippers')
    while not rospy.is_shutdown():
         if param[2] == "angle_1":
            if param[0] > (-0.5):
               param[0]+=(-0.02)

            if param[0] < (-0.5):
                  param[2] = "angle_0"
                  print(param[2])

         elif param[2] == "angle_0":
              rospy.sleep(0.7)
              move_f_1()

         elif param[2] == "angle_2":
            if param[0] < (0.9):
               param[0]+=(0.02)
            if param[0] > (0.9):
               param[2] = "angle_0"
               print(param[2])
               param[1] = "forward_2"
               print(param[1])
               rospy.sleep(4)

         elif param[2] == "angle_3":
            if param[0] > (0):
               param[0]+=(-0.02)
            if param[0] < (0):
               param[2] = "angle_0"
               print(param[2])

         angle.publish(param[0])
         rospy.Rate(30).sleep()


def move_f_1():
   if param[1] == "forward_1":
         end = True
         rate = rospy.Rate(10)
         move_cmd.linear.x = 0.5
         target_time = rospy.Time.now() + rospy.Duration.from_sec(1.5)
         if end == True:
            while rospy.Time.now() < target_time:
                     move.publish(move_cmd)
            else:
                     move_cmd.linear.x = 0
                     move.publish(move_cmd)
                     end = False
                     print(end)

         if end == False:
                  param[1] = "forward_0"
                  param[2] = "angle_2"

   elif param[1] == "forward_2":
         mid = True
         move_cmd.linear.x = 1
         target_time_1 = rospy.Time.now() + rospy.Duration.from_sec(1)
         if mid == True:
            while rospy.Time.now() < target_time_1:
                     move.publish(move_cmd)
            else:
                     move_cmd.linear.x = 0
                     move.publish(move_cmd)
                     mid = False
                     print(mid)

         if mid == False:
                  param[1] = "forward_0"
                  param[2] = "angle_3"



if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
