import params as P
import math

def PointOffset(self,pose,p_dot,plot_vault):
    self.pose = pose
    self.p_dot = p_dot
    self.plot_vault = plot_vault
    def PointOffset(self,P,sheep_mean):
            self.pose = sheep_mean.pose + [P.offset*math.cos(sheep_mean.heading),P.offset*math.sin(sheep_mean.heading)]
            self.p_dot =  - P.kp*self.pose
        
    def Update(self,P,sheep_mean):
            self.pose = sheep_mean.pose + [P.offset*math.cos(sheep_mean.heading),P.offset*math.sin(sheep_mean.heading)]
            self.p_dot =  - P.kp*self.pose
   