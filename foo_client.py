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

           
def init_axis_info(range):
    axis_info = {}
    for axis in foo.ANALOG:
        axis_info[axis] = (AxisInfo(foo.MINMAX[axis][0],foo.MINMAX[axis][1],-foo.SYMMETRIC[axis]*range/(1+foo.SYMMETRIC[axis]),range/(1+foo.SYMMETRIC[axis])))
    return axis_info


def read_gamepad(gamepad, axis_info, cur_vals):
    events = gamepad.read()
    for event in events:
        if 'Absolute' in event.ev_type:
            if event.code in foo.ANALOG: # and abs(event.state) > 2000:
                val_new = axis_info[event.code].transform(event.state)
                cur_vals[event.code] = val_new
        elif 'Key' in event.ev_type:
            pass
        elif 'Sync' in event.ev_type:
            pass
        else:
            print "-----",event.ev_type


def create_msg(cur_vals, deadzone):
    return string.join([str((deadzone < cur_vals[x])*cur_vals[x]) for x in foo.ANALOG],";")


gamepad = inputs.devices.gamepads[0]

address = '127.0.0.1'
port = 9999

freq_1 = 60 # Hz
freq_2 = 120 # Hz

period_1 = 1.0/freq_1
period_2 = 1.0/freq_2


deadzonePerc = 0.1
span = 100
axis_info = init_axis_info(span)
cur_vals = {'ABS_RX': 0,
            'ABS_RY': 0,
            'ABS_RZ': 0,
            'ABS_X':  0,
            'ABS_Y':  0,
            'ABS_Z':  0}


deadzone = deadzonePerc * span
t0 = time.clock()
t_1 = t0
while True:
    t = time.clock()
    if t - t_1 > period_1:
        t_1 = t
        message = create_msg(cur_vals,deadzone)
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        server_address = (address, port)
        sock.connect(server_address)
        try:
            # Send data
            message = create_msg(cur_vals, deadzone)
            print >> sys.stderr, 'sending "%s"' % message
            sock.sendall(message)
            response = sock.recv(1)
            print >> sys.stderr, 'success: "%s"' % response

        finally:
            print >> sys.stderr, 'closing socket'
            sock.close()
    read_gamepad(gamepad, axis_info, cur_vals)


