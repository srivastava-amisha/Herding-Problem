import params as P
import numpy as np

import Generator as Generator
import SheepMean as SheepMean
import Dog as Dog
import Sheep as Sheep
#import Pointoffset as PointOffset
import Goal as Goal
import AngleWrap as AngleWrap
import Animation as Animation
import Delta as Delta
import PointOffset as PointOffset

print(2)

dogs = Generator(P.num_herders,Dog,P)
sheeps = Generator(P.num_walkers,Sheep,P)


sheep_mean = SheepMean(sheeps)
offset_point = PointOffset(P,sheep_mean)
goal = Goal(P,sheep_mean,offset_point)

animator = Animation(P,dogs,sheeps,goal,sheep_mean,offset_point)
count = 0

while np.norm(sheep_mean.pose - goal.pose) >= 0.1 :
    delta = AngleWrap(Delta(P, np.norm(goal.desired_velocity)))

    for j in range(len(dogs)):
        dogs[j].delta_j = delta*(2*j-P.num_herders-1)/(2*P.num_herders - 2)
        dogs[j] = dogs[j].Update(P,sheep_mean,goal)
    
    for i  in range(len(sheeps)):
        sheeps[i] = sheeps[i].Update(P,dogs)
   
    sheep_mean = sheep_mean.Update(sheeps)
    offset_point = offset_point.Update(P,sheep_mean)
    goal = goal.Update(sheep_mean,offset_point)
    animator = animator.Update(P,dogs,sheeps,goal,sheep_mean,offset_point)
    #pause(0.00001)
    count = count + 1

#close(animator.myVideo)