#!/usr/bin/python
# coding=utf-8




import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(7.5) # Initialisierung
try:
  while True:
    p.ChangeDutyCycle(7.0) #1,5ms 90°
    #time.sleep(0.5)
    #p.ChangeDutyCycle(9.8) #1,5ms 90°
    #time.sleep(0.5)
    #p.ChangeDutyCycle(7.5) #1,5ms 90°
    #time.sleep(0.5)
    #p.ChangeDutyCycle(4.3) #1,5ms 90°
    time.sleep(0.5)
except: #KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()