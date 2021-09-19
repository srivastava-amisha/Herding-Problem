# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 16:49:05 2021

@author: sriva
"""

import params as P

def Generator(num_agent,object,P):
    agents = []
    
    for i in range(num_agent):
        agents.append(object(P))

    return agents
    