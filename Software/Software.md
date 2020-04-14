# Software

As operating system on the Raspberry Pi i use the latest Raspbian version.

## ROS
For an easier software management i use the Robot Operating System framework (Version Kinetic)


<p align="center">
  <img src="/images/rosorg_logo.png" width="200"><br>
  <b>Source:www.ros.org</b>
</p>


With this framework it is possible to split the programm in subprogramms which can communicate with each other.

## Steering (PWM Output)
<p align="center">
  <img width="300" src="/images/TiemposServo.png"><br>
  <b>Source:https://de.wikipedia.org/wiki/Servo</b>
</p>

The steering is a short and simple ROS Node. The Node subscribe to the "steering" Topic and gets throught this the requested steering angle.
It gets the angle as a string and convert it back to an integer. The angle is a number between 0 (full left) and 255 (full right).
Out of the requested angle the Node calculate the High phase of the PWM Signal.


## Velocity (CAN Communication)
To run a CAN communication on the Raspberry Pi it is necessary to do some changes on the software settings.
For the settings follow this guidance: https://crycode.de/can-bus-am-raspberry-pi
Additional to the software changes a CAN bus controller is needed. In this project i use the MCP2515. (see Hardware & Electric folder)
After beeing able to send single messages between the motorcontroller and the Raspberry Pi i implemented the communication i a ROS Node. (See folder ROS Nodes)
In this Node i subscribe to the "velocity" Topic to get the requested speed.

## Display (Uart Communication)

