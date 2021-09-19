# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 16:43:21 2021

@author: sriva
"""
import params as P
import numpy as np
import AngleWrap as AngleWrap

class dog():

    def __init__(self,P):
        self.pose = np.random.rand(1,2)*(P.max_bound-P.min_bound)+P.min_bound
        self.delta_j = None
        self.plot_vault = None
        self.desired_pose = None
        self.d_dot = None

    def Update(self,P,sheep_mean,goal):
        away_goal = np.pi + self.delta_j + goal.goal_direction
        away_goal = AngleWrap(away_goal)
        self.desired_pose = sheep_mean.pose + P.d_s_closeness*np.array([[np.cos(away_goal)],[np.sin(away_goal)]])
        self.d_dot = P.kd*(self.desired_pose - self.pose)
        self.pose = self.pose + self.d_dot*P.dt