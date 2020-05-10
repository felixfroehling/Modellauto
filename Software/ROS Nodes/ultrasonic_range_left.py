#!/usr/bin/python
# coding=utf-8

# This node is to get the range from the left front ultrasonic distance sensor.
# Parts of this code are from tutorials-raspberrypi.de
# Link: https://tutorials-raspberrypi.de/entfernung-messen-mit-ultraschallsensor-hc-sr04/


# import Libraries
import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time

# Init the ROS node and set Publisher
ultrasonicRangeLeft = rospy.Publisher('ultrasonicRangeLeft', String, queue_size=10)
rospy.init_node('ultrasonicRangeLeft', anonymous=True)    

# GPIO Mode
GPIO.setmode(GPIO.BCM)

# GPIO Pins for right ultrasonic range sensor
GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # Trigger high
    GPIO.output(GPIO_TRIGGER, True)
    
    # wait 0.01ms and set Trigger low
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime =  time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    
    dist = (TimeElapsed * 34300) / 2
    
    return dist

if __name__ == '__main__':
    try:
        while True:
            actualDistance = distance()
            ultrasonicRangeLeft.publish(str(actualDistance))
            print("Gemessene Entfernung = %.1f cm" % actualDistance)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Stop")
        GPIO.cleanup()