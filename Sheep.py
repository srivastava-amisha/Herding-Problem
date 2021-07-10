import numpy as np

class Sheep():

    def __init__(self,P):
        self.pose = np.random.rand(1,2)*P.herd_radius+P.herd_center
        self.heading = np.random.rand(1,1)*2*np.pi

    def Update(self,P,dogs):
        self.s_dot = np.array([0,0])
        for k in range(len(dogs)):
            self.s_dot = self.s_dot + (-dogs[k].pose + self.pose)/(np.linalg.norm(dog[k].pose - self.pose)**3)

        angle_arithmetic = AngleWrap(np.arctan(self.s_dot[1],self.s_dot[0])) - self.heading
        self.heading = self.heading + P.dt*angle_artihmetic
        self.pose = self.pose + np.linalg.norm(P.dt*self.s_dot)*np.array([np.cos(self.heading),np.sin(self.heading)])
