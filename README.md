# Modellauto
A home project for the electrification and automation of a model car by Felix Fröhling <br />
This Project has no specific goal and is just for fun.

Project started on 16.03.2020

Documentation started on 02.04.2020


## Table of contents
- README
- Hardware and Electric (Description of used components)
- Software (Description of Software)
- images (all used images)


## Car Profile Picture
<img src="/images/car_outdoor_08.05_2.jpg" width="600">

## Project Description
### Hardware
The modelcar is build around a raspberry Pi 4 with Raspbian as operating system.
As chassis i used an old RC buggy and replaced the combustion engine with an electric motor.
The electric motor has a seperate controller which communicate via CAN bus with the raspberry Pi.
In the front i added two ultrasonic distance sensors and a Picamera.
Additionally to this, a Display with 5 buttons is mounted on the top for live informations.
For further information take a look in the "Hardware & Electric" folder.
### Software
For the software i use the Robot Operating System as framework, so i can combine smaller programms to a funktional system.
Every Sensor and actuator has its own programm called "Node" and communicate with the other Nodes over the framework.
So i can edit and test each subsystem on its own. The Nodes can be found in the "Software" folder.

# TODO
- Battery supply of the engine
- Finish Startup menu on the display
- first field tests
- import face detection and tracking into ROS framework
- "follow the line" project with the camera


# Tasks done
- face detection and tracking with camera (Done, up to 8 fps)
- Write python program to control the car with a gaming controller (Done, see Software/ROS-Nodes/gamecontroller_input.py)
- Image processing with python, so the car can follow a black line
- connect a display to Raspberry Pi (UART connection) (Done, See Software/ROS-Nodes/display_uart.py)
