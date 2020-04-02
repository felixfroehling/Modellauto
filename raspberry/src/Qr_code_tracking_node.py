#!/usr/bin/python
# coding=utf-8

# import the necessary packages
from picamera.array import PiRGBArray
import picamera 
import time
import cv2
import numpy as np
import sys
import time
import math
#Import for ROS
import rospy
from std_msgs.msg import String

camera = picamera.PiCamera()
output = np.empty((240, 320, 3), dtype=np.uint8)
qrCodeDetector = cv2.QRCodeDetector()
ErrorCount = 0

def initCam():
    #set Camera settings
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)
    
def imageProcessing(image):
    global ErrorCount
    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
    if points is not None:
        ErrorCount = 0
        p1 = points[0][0]
        p2 = points[0][2]
        #print(points)
        p_middle = int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2)
        calculate_movement(p_middle)
        #print(p_middle)
    else:
        print(str("Error, no QR Code found!"))
        if ErrorCount <= 5:
            ErrorCount = ErrorCount+1
        else:
            #pub_steering.publish(str(0))
            print(str("Error > 5"))
    #print("Berechnung: abs(" + str(p1[0]) + "-" + str(p2[0]) + ") und abs(" + str(p1[1]) + "-" + str(p2[1]) + ")")
    #print("Genauer: (" + str(abs(p1[0]-p2[0])) + ") und (" + str(abs(p1[1]-p2[1])) + ")")
    #return p_middle

def calculate_movement(middle):
    if middle[0] <= 60:
        #pub_steering.publish(str(-50))
        print(str(-50))
    elif middle[0] >= 260:
        #pub_steering.publish(str(50))
        print(str(50))
    else:
        x_point = (middle[0] -160)/2
        #pub_steering.publish(str(x_point))
        print(str(x_point))

               

pub_steering = rospy.Publisher('steering', String, queue_size=10)
rospy.init_node('QR_Code_Node', anonymous=True)

initCam()

while True:
        
    camera.capture(output, 'rgb')
    #output = cv2.imread('download.jpg')
    imageProcessing(output)
    
    #time.sleep(1)

    #cv2.imshow("Image", output)
        
    #cv2.waitKey(0)
    #cv2.destroyWindow('Image')



