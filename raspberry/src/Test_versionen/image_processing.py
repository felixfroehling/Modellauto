

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


with picamera.PiCamera() as camera:
    #set Camera settings
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)
    # Get and save image from camera
    #output = np.empty((240, 320, 3), dtype=np.uint8)
    #camera.capture(output, 'rgb')
    output = cv2.imread('download.jpg')
    # convert rgb image to gray image
    #gray_image = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    # find QR code in gray image
    # Source: https://docs.opencv.org/3.4/de/dc3/classcv_1_1QRCodeDetector.html
    qrCodeDetector = cv2.QRCodeDetector()
    decodedText, points, _ = qrCodeDetector.detectAndDecode(output)
    # plot rectangles of found qr codes in gray image
    print(points[0][0])
    print(points[0][1])
    print(points[0][2])
    print(points[0][3])
    output = cv2.line(output, tuple(points[0][0]), tuple(points[0][1]), (255,0,0), 5)
    output = cv2.line(output, tuple(points[0][1]), tuple(points[0][2]), (255,0,0), 5)
    output = cv2.line(output, tuple(points[0][2]), tuple(points[0][3]), (255,0,0), 5)
    output = cv2.line(output, tuple(points[0][3]), tuple(points[0][0]), (255,0,0), 5)
    
    cv2.imshow("Image", output)
    cv2.waitKey(0)
    cv2.desytroyAllWindows()
    
    #if points is not None:
        
        #nrOfPoints = len(points)
        
        #for i in range(nrOfPoints):
            #print(i)
            #print(range(nrOfPoints))
            #s = 'print rectange'
            #print(points)
            #nextPointIndex = (i+1) % nrOfPoints
            #cv2.line(output, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 5)
            #print(points[i][0])
            #print(points[nextPointIndex][0])
        #cv2.line(output, points[1][0], points[2][0], (0,0,255), 5)  
        #print(decodedText)
        
        #cv2.imshow("Image", output)
        #cv2.imwrite('marked_image.jpg', output)
        #cv2.waitKey(0)
        #cv2.desytroyAllWindows()
        
    #else:
        #s = "no QR code detected"
        #print(s)
                     
    
    
    
    
    

    
    #camera.start_preview()
    #time.sleep(5)
    #image = camera.capture()
    #gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #camera.capture('/home/pi/Desktop/image3.jpg')
    #cv2.imwrite('gray_image.jpg', gray)
    #camera.stop_preview()

#while True:
#    image = camera.read()
#    cv2.imshow('image',image)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()