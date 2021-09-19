# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 16:49:51 2021

@author: sriva
"""
import params as P
import numpy as np

class Goal():

    def __init__(self,P,sheep_mean,offset_point):
        self.pose = np.random.rand(1,2)*(P.max_bound-P.min_bound)+P.min_bound
        self.goal_direction = self.pose - sheep_mean.pose
        self.desired_velocity = self.goal_direction*offset_point.p_dot
        self.goal_direction = np.arctan(self.goal_direction[1],self.goal_direction[0])
        self.plot_vault = None

    def Update(self,sheep_mean,offset_point):
        self.goal_direction = self.pose - sheep_mean.pose
        self.desired_velocity = self.goal_direction*offset_point.p_dot
        self.goal_direction = np.arctan(self.goal_direction[1],self.goal_direction[0])