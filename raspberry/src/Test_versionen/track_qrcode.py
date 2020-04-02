# import the necessary packages
from picamera.array import PiRGBArray
import picamera 
import time
import cv2
import numpy as np
import sys
import time
import math

camera = picamera.PiCamera()
output = np.empty((240, 320, 3), dtype=np.uint8)
qrCodeDetector = cv2.QRCodeDetector()

def initCam():
    #set Camera settings
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)
    
def imageProcessing(image):
    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
    p1 = points[0][0]
    p2 = points[0][2]
    print(points)
    p_middle = int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2)
    print(p_middle)
    #print("Berechnung: abs(" + str(p1[0]) + "-" + str(p2[0]) + ") und abs(" + str(p1[1]) + "-" + str(p2[1]) + ")")
    #print("Genauer: (" + str(abs(p1[0]-p2[0])) + ") und (" + str(abs(p1[1]-p2[1])) + ")")
    image = cv2.line(image, p_middle, p_middle, (0,255,0), 5)
    image = cv2.line(image, (0,240), (0,240), (0,0,255), 5)
    image = cv2.line(image, tuple(points[0][0]), tuple(points[0][1]), (255,0,0), 5)
    image = cv2.line(image, tuple(points[0][1]), tuple(points[0][2]), (255,0,0), 5)
    image = cv2.line(image, tuple(points[0][2]), tuple(points[0][3]), (255,0,0), 5)
    image = cv2.line(image, tuple(points[0][3]), tuple(points[0][0]), (255,0,0), 5)
    return image
#def getImage():


#def getMiddle(p1, p2):

#    return pMiddle


initCam()
    
camera.capture(output, 'rgb')
#output = cv2.imread('download.jpg')
output = imageProcessing(output)


cv2.imshow("Image", output)
    
cv2.waitKey(0)
cv2.destroyWindow('Image')


