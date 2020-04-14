#!/usr/bin/python
# coding=utf-8

#This Node is used to grap the gamecontroller data and publish it in ROS
#The left joystick (Y-Abs) is to controll the velocity and the right joystick (X-Abs) for the steering
#The program is event-triggert and publish the new data at every gamepad event
#Credits to Felix Fröhling

from evdev import InputDevice, categorize, ecodes
import rospy
from std_msgs.msg import String

pub_steering = rospy.Publisher('steering', String, queue_size=10)
pub_velocity = rospy.Publisher('velocity', String, queue_size=10)
rospy.init_node('gamecontroller', anonymous=True)    #tcp_comm

gamepad = InputDevice('/dev/input/by-id/usb-Goodbetterbest_Ltd_Gioteck_VX2_2.4G_Wireless_Controller-event-joystick')

#button code variables (Event Code)
Kreuz = 306
Viereck = 307
Dreieck = 304
Kreis = 305

JoyLeftHorizontal = 0
JoyLeftVertical = 1
JoyRightHorizontal = 2
JoyRightVertical = 5

#Print the gamepad name
print(gamepad)

#loop and filter
for event in gamepad.read_loop():
    # 
    if event.code == JoyRightHorizontal:
        msg = str(event.value)          #get joystick value and convert into string
        pub_steering.publish(msg)       #publish streering (value between 0-255)
    if event.code == JoyLeftVertical:
        msg = str(event.value)          #get joystick value and convert into string
        pub_velocity.publish(msg)       #publish velocity (value between 0-255)

        
        