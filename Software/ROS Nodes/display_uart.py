#!/usr/bin/python
# coding=utf-8 

#This Node is used to write data on the Display
#The data is send via uart. All data with"\033..." are commands like color or position.
#Till now only the requested velocity and steering are monitored.
#The display has also buttons, which are not implemented till now. Update follows...
#Credits to Felix Fröhling

import rospy
from std_msgs.msg import String, Int32
import serial
from time import sleep

#If new velocity data is published this function send the new data to the display
def velocityCallback(data):
    ser.write("\033[6;10f")
    msg = data.data
    ser.write(msg)
    ser.write("  ")
    
#If new steering data is published this function send the new data to the display
def steeringCallback(data):
    ser.write("\033[4;10f")
    msg = data.data
    ser.write(msg)
    ser.write("  ")

rospy.init_node('Velocity_Node', anonymous=True)
rospy.Subscriber("velocity", String, velocityCallback)
rospy.Subscriber("steering", String, steeringCallback)

ser = serial.Serial ("/dev/ttyS0", 115200)    #Open serial port with baud rate

ser.write("\033[2J\033[f\033[?7h")
ser.write("\033(D")                  #Change font size
ser.write("Fahrparameter:")
ser.write("\033(C")                  #Change font size
ser.write("\033[4;1fSteering:")      #Set curser and print data
ser.write("\033[6;1fVelocity:")      #Set curser and print data
ser.write("\033[4;10f")              #Set curser
ser.write("000")                     #print initial value
ser.write("\033[6;10f")              #Set curser
ser.write("000")                     #print initial value


while True:
    
    eingabe = input("Ihre Eingabe ")
    if eingabe == quit:
        break
    sleep(0.5)
    
    #The following lines are for receiving data. Not implemented yet...
    
    #received_data = ser.read()              #read serial port

    #data_left = ser.inWaiting()             #check for remaining byte
    #received_data += ser.read(data_left)
    #print (received_data)                   #print received data
    #ser.write(received_data)                #transmit data serially
    


