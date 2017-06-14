# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 19:42:15 2017

@author: John Smith
"""

import socket
import sys
import RPi.GPIO as GPIO

import foo_common as foo

address = "192.168.1.32"
port = 9999

duty_cycle = 100

# Prepare PWMs
GPIO.setmode(GPIO.BCM)
[GPIO.setup(pin, GPIO.OUT) for pin in foo.GPIOS]
PWMs = [GPIO.PWM(pin, duty_cycle) for pin in foo.GPIOS]
[pwm.start(0) for pwm in PWMs]

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = (address, port)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    try:
        data = connection.recv(128)
        if data:
            connection.sendall("1")
        else:
            connection.sendall("0")
            data = "NULL"
        vals = [int(x) for x in data.split(';')]
	for i in range(6):
           PWMs[i].ChangeDutyCycle(abs(vals[i]))

#        print >> sys.stderr, data
    finally:
        # Clean up the connection
        connection.close()

sock.close()
