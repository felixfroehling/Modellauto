#!/usr/bin/python
# coding=utf-8

import rospy
from std_msgs.msg import String, Int32

import RPi.GPIO as GPIO
import time



def callback(data):
    #print("got data")
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    buf = float(data.data)
    print(buf)
    #print(type(buf))
    changeSteering(buf)
    #data = buf.decode('utf-8')
    #dataMessage = data.split(' ', 1)
    #state = dataMessage[0]
    #value = dataMessage[1]
    
    
def changeSteering(value):
    #Value is between -50 and 50
    output_value = 5.5 * (value+50)/100 + 4.3
    p.ChangeDutyCycle(output_value)
    #value += 30    #ofset 0 - 100
    #p.ChangeDutyCycle(value)


rospy.init_node('Steering_Node', anonymous=True)
rospy.Subscriber("steering", String, callback)

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(7) # Initialisierung
try:
  while True:
    #global state
    ##if state == 'go':
    #    p.ChangeDutyCycle(5)
    #elif state == 'stop':
    #    p.ChangeDutyCycle(12.5)
    eingabe = input("Ihre Eingabe ")
    if eingabe == quit:
        break
    #p.ChangeDutyCycle(7.5) #1,5ms 90°
    #time.sleep(0.5)
except: #KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
