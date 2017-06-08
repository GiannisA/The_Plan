# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 19:44:03 2017

@author: John Smith
"""


import time
import socket
import sys
import numpy as np
import exceptions as exc
import string
import inputs
import foo_common as foo


class AxisInfo:
    def __init__(self,_min,_max,cap_min, cap_max):
        if _min >= _max:
            raise exc.Exception("min is not less than max")
        self.min = _min
        self.max = _max
        self.cap_min = cap_min
        self.cap_max = cap_max
        self.multipier = (cap_max-cap_min)/((self.max-self.min)*1.0)
        self.val_cur = self.transform(self.min)

    def transform(self,val_in):
        return int((val_in-self.min)*self.multipier+self.cap_min)
    
    def update(self,val_in):
        self.val_cur = self.transform(val_in)

    def set_val_cure(self,val_cur):
        self.val_cur = val_cur
    
    def get_val_cur(self):
        return self.val_cur
           
def normalise_axis_info(range):
    axis_info = []
    for i in foo.SIZE:
        axis_info.append(AxisInfo(foo.MINMAX[i][0],foo.MINMAX[i][1],-foo.SYMMETRIC[i]*range/(1+foo.SYMMETRIC[i]),range/(1+foo.SYMMETRIC[i]))
    return axis_info

def main_foo(gamepad, normalised_axis):
    while True:
        events = gamepad.read()
        for event in events:
            if 'Absolute' in event.ev_type:
                if event.code in analog: # and abs(event.state) > 2000:
                    val_new = normalised_axis[event.code].update(event.state)
                    print  string.join([x[0]+":"+str(x[1].get_val_cur()) for x in normalised_axis.iteritems()],";")
            elif 'Key' in event.ev_type:
                print "--",event.code,'-',event.state
            elif 'Sync' in event.ev_type:
                pass
            else:
                print "-----",event.ev_type
        time.sleep(0.001)


def update_values():
    pass


def create_msg():
    return "=== MESSAGE ==="


address = 'localhost'
port = 10000

freq_1 = 60 # Hz
freq_2 = 120 # Hz

period_1 = 1.0/freq_1
period_2 = 1.0/freq_2




t0 = time.clock()
t_1 = t0

while True:
    t = time.clock()
    if t - t_1 > period_1:
        t_1 = t
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        server_address = (address, port)
        sock.connect(server_address)
        try:
            # Send data
            message = create_msg()
            print >> sys.stderr, 'sending "%s"' % message
            sock.sendall(message)
            response = sock.recv(1)
            print >> sys.stderr, 'success: "%s"' % response

        finally:
            print >> sys.stderr, 'closing socket'
            sock.close()
    update_values()


