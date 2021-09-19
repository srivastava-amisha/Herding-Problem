# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 21:13:18 2021

@author: sriva
"""
import matplotlib.pyplot as plt
import matplotlib
import math

class Animation :
    def __init__(self,sheep_body_size,figure,encirclement,frames,myVideo):
        self.sheep_body_size = sheep_body_size
        self.figure = figure 
        self.encirclement = encirclement
        self.frames = frames
        self.myVideo = myVideo
        
    def Animation(self,P,dogs,sheeps,goal,sheep_mean,offset_point):
        self.sheep_body_size = P.sheep_body_size
        self.figure = matplotlib.pyplot.figure()
        for i in range(len(dogs)):
            dogs[i].plot_vault = plt.plot(dogs[i].pose[1],dogs[i].pose[2])
            for i in range(len(sheeps)):
                sheeps[i].plot_vault = plt.quiver(sheeps[i].pose[1],sheeps[i].pose[2],self.sheep_body_size*math.cos(sheeps[i].heading),self.sheep_body_size*math.sin(sheeps[i].heading),'-ob')
            goal.plot_vault = plt.plot(goal.pose(1),goal.pose(2),'ok','MarkerSize',50)
            sheep_mean.plot_vault = plt.plot(sheep_mean.pose[1],sheep_mean.pose[2],'.g','MarkerSize',20)
            offset_point.plot_vault = plt.plot(offset_point.pose[1],offset_point.pose[2],'.k','MarkerSize',20)
        self.encirclement = matplotlib.patches.Circle((sheep_mean.pose),P.d_s_closeness)
        plt.xlim([-10,40])
        plt.ylim([-10,40])
        #self.frames = [getframe(self.figure)]

    def Update(self,P,dogs,sheeps,goal,sheep_mean,offset_point):
            for i in range(len(dogs)):
                dogs[i].plot_vault = plt.plot(dogs[i].pose[1],dogs[i].pose[2],'.r','MarkerSize',20)
            for i in range(len(sheeps)):
                sheeps[i].plot_vault = plt.quiver(sheeps[i].pose[1],sheeps[i].pose[2],self.sheep_body_size*math.cos(sheeps[i].heading),self.sheep_body_size*math.sin(sheeps[i].heading),'-ob')
            goal.plot_vault = plt.plot(goal.pose[1],goal.pose[2],'ok','MarkerSize',50)
            sheep_mean.plot_vault = plt.plot(sheep_mean.pose[1],sheep_mean.pose[2],'.g','MarkerSize',20)
            offset_point.plot_vault = plt.plot(offset_point.pose[1],offset_point.pose[2],'.k','MarkerSize',20)
            self.encirclement = matplotlib.patches.Circle(sheep_mean.pose,P.d_s_closeness)
            plt.xlim([-10,40])
            plt.ylim([-10,40])
            #self.frames = [self.frames,getframe(self.figure)];