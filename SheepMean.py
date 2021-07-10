import numpy as np

class SheepMean():

    def __init__(self,sheeps):
        self.pose = np.array([0,0])
        self.heading = 0
        
        for i in range(len(sheeps)):
            self.pose = self.pose + sheeps[i].pose
            self.heading = self.heading + sheeps[i].heading

        self.pose = self.pose/len(sheeps)
        self.heading = self.heading/len(sheeps)
    
    def Update(self,sheeps):
        self.pose = np.array([0,0])
        self.heading = 0
        
        for i in range(len(sheeps)):
            self.pose = self.pose + sheeps[i].pose
            self.heading = self.heading + sheeps[i].heading

        self.pose = self.pose/len(sheeps)
        self.heading = self.heading/len(sheeps)
