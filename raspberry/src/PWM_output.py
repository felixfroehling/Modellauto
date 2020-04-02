#!/usr/bin/python
# coding=utf-8

# With this Node the Servomotor is controlled by a simple PWM Signal
# The Servomotor is used for the steering
# Credits to Felix Fröhling


# Import for ROS
import rospy
from std_msgs.msg import String, Int32

# Import for the PWM Signal generation
import RPi.GPIO as GPIO
import time



def callback(data):
    # Callback 0
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)  # Debug information
    buf = float(data.data)
    print(buf)
    #print(type(buf))
    changeSteering(buf)
    
    
def changeSteering(value):
    # Value is between -50 and 50
    # +50 is full right, -50 is full left
    output_value = 5.5 * (value+50)/100 + 4.3
    p.ChangeDutyCycle(output_value)   # Set PWM cicle


rospy.init_node('Steering_Node', anonymous=True)
rospy.Subscriber("steering", String, callback)

# Initialization for GPIO 17 (PWM output Pin)
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 as PWM output pin with 50Hz
p.start(7) # Start PWM output
try:
  while True:
    # p.changeDutyCycle(7.5)  #  1,5ms High means 90°. So steering is straight
    eingabe = input("Ihre Eingabe ")
    if eingabe == "quit":
        break

except: #KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
