#!/usr/bin/python
# coding=utf-8

import rospy
import can

from std_msgs.msg import String

# For Threading
from time import sleep
import threading 
import time

class RepeatedTimer(object):
  def __init__(self, interval, function, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False

def updateCAN(current_speed):
    global speed
    #print("speed: " + str(speed))
    #print("updated CAN")
    #print(current_speed)
    changeVelocity(speed)

speed = 127
rt = RepeatedTimer(0.1, updateCAN, speed)

# CAN Bus


can_interface = 'can0'
bus = can.interface.Bus(can_interface, bustype='socketcan_native')

def callback(data):
    global speed
    speed = int(data.data)
    print(speed)


def changeVelocity(inputSpeed):
    # speed is between 0 and 255
    currentHigh = 0x04
    currentLow = 0x00
    speedHigh = 0x04
    speedLow = 0x00
    
    speed = 127-inputSpeed
    #print(str(speed))
    
    if (speed <= 2 and speed >= -2):
        currentHigh = 0x00
        currentLow = 0x00
        speedHigh = 0x00
        speedLow = 0x00
        #print(str("speed = 0"))
    else:
        speed = int(speed * (2048/127))
        speedHigh = (speed >> 8) & 0x00FF
        speedLow = speed & 0x00FF
        #print("speed: " + str(speedHigh) + " " + str(speedLow))
    
    #print(speedHigh)
    #print(speedLow)
    msg = can.Message(arbitration_id=0x210,data=[currentHigh,currentLow,speedHigh,speedLow,0,0,0,0],extended_id=False)
    bus.send(msg)


rospy.init_node('Velocity_Node', anonymous=True)
rospy.Subscriber("velocity", String, callback)


while True:
    eingabe = input("Ihre Eingabe ")
    if eingabe == "quit":
        rt.stop() # better in a try/finally block to make sure the program ends
        break
    #print("banana")
