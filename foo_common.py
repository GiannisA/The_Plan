# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 19:54:53 2017

@author: John Smith
"""

SIZE=6

LS_X = 0
LS_Y = 1
RS_X = 2
RS_Y = 3
LT   = 4
RT   = 5

ANALOG = ('ABS_X',
          'ABS_Y',
          'ABS_RX',
          'ABS_RY',
          'ABS_Z',
          'ABS_RZ')


SYMMETRIC = {'ABS_RX': True,
             'ABS_RY': True,
             'ABS_RZ': False,
             'ABS_X':  True,
             'ABS_Y':  True,
             'ABS_Z':  False}

MINMAX = {'ABS_RX': [-32767, 32767],
          'ABS_RY': [-32767, 32767],
          'ABS_RZ': [0, 255],
          'ABS_X': [-32767, 32767],
          'ABS_Y': [-32767, 32767],
          'ABS_Z': [0, 255]}

GPIOS = (20,
         16,
         24,
         23,
         6,
         5)
