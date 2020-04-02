#!/usr/bin/python
# coding=utf-8

import rospy
import can

from std_msgs.msg import String


can_interface = 'can0'
bus = can.interface.Bus(can_interface, bustype='socketcan_native')

def callback(data):
    buf = int(data.data)  
    print(buf)
    changeVelocity(buf)


def changeVelocity(speed):
    currentHigh = 0x04
    currentLow = 0x00
    speedHigh = 0x04
    speedLow = 0x00
    
    speed = int(speed * (1024/70))
    
    if speed == 0:
        currentHigh = 0x00
        currentLow = 0x00
        speedHigh = 0x00
        speedLow = 0x00
        print(str("speed = 0"))
    else:
        speedHigh = (speed >> 8) & 0x00FF
        speedLow = speed & 0x00FF
        print("speed: " + str(speedHigh) + " " + str(speedLow))
    
    msg = can.Message(arbitration_id=0x210,data=[currentHigh,currentLow,speedHigh,speedLow],extended_id=False)
    bus.send(msg)


rospy.init_node('Velocity_Node', anonymous=True)
rospy.Subscriber("velocity", String, callback)


while True:
    eingabe = input("Ihre Eingabe ")
    if eingabe == quit:
        break

