import numpy as np

def AngleWrap(angle):
    while angle < 0:
        angle = angle + 2*np.pi
    
    while angle > 2*pi:
        angle = angle - 2*pi
    
    return angle
