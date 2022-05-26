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

    nachalo = True
    rospy.init_node('control_flippers')
    while not rospy.is_shutdown():
      if nachalo == True:
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
            if param[0] < (0.3):
               param[0]+=(0.01)
               #print(param[0])

            if param[0] > (0.3):
               param[2] = "angle_0"
               print(param[2])
               #rospy.sleep(0.7)
               param[1] = "forward_3"
               param[2] = "angle_3"
               print(param[1])

         elif param[2] == "angle_3":
            if param[0] < (1.2):
               param[0]+=(0.04)
               #print(param[0])

            if param[0] > (1.2):
               param[2] = "angle_0"
               print(param[2])


         elif param[2] == "angle_4":
            if param[0] > (0):
               param[0]+=(-0.0075)
               #print(param[0])

            if param[0] < (0):
               param[2] = "angle_0"
               param[1] = "forward_0"
               print(param[2])


         rospy.Rate(100).sleep()
         angle.publish(param[0])


def move_f_1():

   if param[1] == "forward_1":
         end = True
         move_cmd.linear.x = 0.2
         target_time = rospy.Time.now() + rospy.Duration.from_sec(3.75)
         if end == True:
            while rospy.Time.now() < target_time:
                     move.publish(move_cmd)
            else:
                     end = False
                     param[1] = "forward_2"

         if end == False:
                  param[2] = "angle_2"
                  #param[1] = "forward_2"

   if param[1] == "forward_2":
        mid = True
        move_cmd.linear.x = 0.15
        move.publish(move_cmd)
        #target_time_1 = rospy.Time.now() + rospy.Duration.from_sec(0.5)
        #if mid == True:
            #while rospy.Time.now() < target_time_1:
                     #move.publish(move_cmd)
            #else:
                     #mid = False
                     #print(mid)

        #if mid == False:
                  #param[1] = "forward_0"
                  #print(param[2])

   if param[1] == "forward_3":

        move_cmd.linear.x = 0.065
        check = True
        target_time_1 = rospy.Time.now() + rospy.Duration.from_sec(3.8)

        if check == True:
           while rospy.Time.now() < target_time_1:
                    move.publish(move_cmd)
           else:
                    check = False
                    param[1] = "forward_4"

        if check == False:
                 param[2] = "angle_4"

   if param[1] == "forward_4":
        move_cmd.linear.x = 0.14
        #check_1 = True
        move.publish(move_cmd)
        #rospy.sleep(0.2)
        #target_time_2 = rospy.Time.now() + rospy.Duration.from_sec(1)

        #if check_1 == True:
           #while rospy.Time.now() < target_time_2:
                    #move.publish(move_cmd)
           #else:
                    #check_1 = False
                    #param[1] = "forward_0"

        #if check_1 == False:
                 #param[2] = "angle_4"
                 #param[1] = "forward_0"


   if param[1] == "forward_0":
        move_cmd.linear.x = 0
        move.publish(move_cmd)




if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass