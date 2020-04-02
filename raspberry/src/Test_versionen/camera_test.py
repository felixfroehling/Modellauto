#source: https://pythonprogramming.net/raspberry-pi-camera-opencv-face-detection-tutorial/

import io
import picamera
import cv2
import numpy as np
import sys
import time

#Create a memory stream so photos doesn't need to be saved in a file
#stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
#with picamera.PiCamera() as camera:
#    camera.resolution = (320, 240)
#    camera.capture(stream, format='jpeg')

#Convert the picture into a numpy array
#buff = np.fromstring(stream.getvalue(), dtype=numpy.uint8)

#Now creates an OpenCV image
#inputImage = cv2.imdecode(buff, 1)

#Load a cascade file for detecting faces
#face_cascade = cv2.CascadeClassifier('/home/pi/ros_catkin_ws/src/raspberry/src/Test_versionen/faces.xml')

#Convert to grayscale
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Display barcode and QR code location

inputImage = cv2.imread("qrcode.jpg")

def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)
    # Display results
    cv2.imshow("Results", im)

qrDecoder = cv2.QRCodeDetector()

# Detect and decode the qrcode
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
if len(data)>0:
    print("Decoded Data : {}".format(data))
    display(inputImage, bbox)
    rectifiedImage = np.uint8(rectifiedImage);
    cv2.imshow("Rectified QRCode", rectifiedImage);
else:
    print("QR Code not detected")
    cv2.imshow("Results", inputImage)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
