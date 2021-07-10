import numpy as np

class P():

    def __init__(self):
        # Animation params
        self.min_bound = 0
        self.max_bound = 10
        self.dt = 0.1

        # Model Initialisation
        self.num_herders = 3
        self.num_walkers = 5
        self.herd_radius = 5
        self.herd_center = np.random.rand(1,2)*(self.max_bound-self.min_bound-1)+self.min_bound+1
        self.sheep_body_size = 0.7
        self.offset = 2
        self.d_s_closeness = 6
        self.kp = 0.5
        self.kd = 2


