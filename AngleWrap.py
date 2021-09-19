# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 16:48:30 2021

@author: sriva
"""

import numpy as np

def AngleWrap(angle):
    while angle < 0:
        angle = angle + 2*np.pi
    
    while angle > 2*pi:
        angle = angle - 2*pi
    
    return angle