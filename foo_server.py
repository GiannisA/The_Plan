# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 19:42:15 2017

@author: John Smith
"""

import socket
import sys

address = '127.0.0.1'
port = 9999

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
        print >> sys.stderr, data
    finally:
        # Clean up the connection
        connection.close()

sock.close()