from picamera import PiCamera
from time import sleep

camera = PiCamera()

image = camera.capture()
write