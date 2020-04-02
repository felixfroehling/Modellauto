#!/usr/bin/python
# coding=utf-8


import rospy
from std_msgs.msg import String

# for GPIO pin usage
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!")

import time
import signal
import sys

# Variable
state = ""

##
## GPIO stuff
##
GPIO.setmode(GPIO.BCM) # use the GPIO names, _not_ the pin numbers on the board
# Raspberry Pi pin configuration:
# pins	    BCM   BOARD
ledPin    = 18 # pin 12

# GPIO setup
print('GPIO setup...')
GPIO.setup(ledPin, GPIO.OUT)


# my signal handler
def sig_handler(_signo, _stack_frame):
    # clear display
    # GPIO cleanup
    GPIO.cleanup()
    print "led_blinky terminated clean."
    sys.exit(0)

# signals to be handled
signal.signal(signal.SIGINT,  sig_handler)
signal.signal(signal.SIGHUP,  sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

# Subscriber

def callback(data):
    global state
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    buf = data.data
    data = buf.decode('utf-8')
    dataMessage = data.split(' ', 1)
    state = dataMessage[0]


rospy.init_node('PWM_output', anonymous=True)
rospy.Subscriber("tcp_message", String, callback)

time_high = 0.0015	#HIGH for 1.5 ms

while (True):
    global state
    print(state)
    if state == 'go':
        print("GO")
        time_high = 0.001	#HIGH for 1 ms
        
    elif state == 'stop':
        print("STOP")
        time_high = 0.002
    else:
        print("OTHER")
        

    GPIO.output(ledPin, GPIO.LOW)     #PIN HIGH
    time.sleep(time_high)
    GPIO.output(ledPin, GPIO.HIGH)    #PIN LOW
    time.sleep(0.02-time_high)
