# import the necessary packages
from picamera.array import PiRGBArray
import picamera 
import time
import cv2
import numpy as np
import sys
import time


with picamera.PiCamera() as camera:
    #set Camera settings
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)
    camera.capture('test_image.jpg')