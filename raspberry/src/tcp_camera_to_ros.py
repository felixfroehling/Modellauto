#!/usr/bin/python
# coding=utf-8


import socket
import rospy
from std_msgs.msg import String

host = ''
port = 5570



def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

#def GET():
#    reply = storedValue
#    return reply

#def REPEAT(dataMessage):
#    reply = dataMessage[1]
#    return reply

def dataTransfer(conn):
    #Publisher
    pub_steering = rospy.Publisher('steering', String, queue_size=10)
    #pub_velocity = rospy.Publisher('velocity', String, queue_size=10)
    rospy.init_node('tcp_camera_to_ros_Node', anonymous=True)    #tcp_comm

    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        # Split the data such that you separate the command
        # from the rest of the data.
        #print("Data: " + data)
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        pub_steering.publish(command)
        print(str(command))
        #else:
        #    print("Wrong Data!")
            #reply = REPEAT(dataMessage)
            #print(reply)
        # Send the reply back to the client
        #conn.sendall(str.encode(reply))
        #print("Data has been sent!")
    conn.close()
        

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        s.close()
        break

