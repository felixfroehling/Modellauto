# Hardware and Electric Components

In this document I will give a short overview of the used hardware components and their connection.
As basis i use a RC-Buggy chassis where replaced the combustion engine with a electric engine.
The steering is controlled by a servomotor.

<img src="/images/chassis.jpg" width="600">

## Raspberry Pi

As main controller i use a Raspberry Pi 4 Modell 4 with 4GB RAM.
## ----Raspberry Pi Picture-----

## Motorcontroller

##------Motorcontroller Picture------

## MCP2515 CAN Module
For the communication between the Raspberry Pi and the Motorcontroller we need the MCP2515 Can module.
This module is necessary because the Raspberry Pi has no CAN communication and the Motorcontroller is controlled by CAN messages.


##-------MCP2515 Picture --------
