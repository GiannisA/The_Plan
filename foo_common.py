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


SYMMETRIC = (True,
             True,
             True,
             True,
             False,
             False)


MINMAX = ((-32767, 32767),
          (-32767, 32767),
          (-32767, 32767),
          (-32767, 32767),
          (0, 255),
          (0, 255))



