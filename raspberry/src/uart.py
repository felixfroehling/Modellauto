#!/usr/bin/python
# coding=utf-8

import serial
from time import sleep

def callback(data):
    ser.write(data)
    print("Daten gesendet")

rospy.init_node('Velocity_Node', anonymous=True)
rospy.Subscriber("velocity", String, callback)

ser = serial.Serial ("/dev/ttyS0", 115200)    #Open port with baud rate


while True:
    #ser.write("Hallo, hier ist Raspi 4")
    #print("Nachricht gesendet")
    
    #received_data = ser.read()              #read serial port
    #sleep(0.5)
    #data_left = ser.inWaiting()             #check for remaining byte
    #received_data += ser.read(data_left)
    #print (received_data)                   #print received data
    #ser.write(received_data)                #transmit data serially
    
    

    sleep(1)

