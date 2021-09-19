import math

def Delta(P,desired_velocity):
    def func(d) :
        f= math.sin(P.num_herders*d/(2-2*P.num_herders))/(P.d_s_closeness^2 *math.sin(d/(2-2*P.num_herders))) - desired_velocity 
        return f
    reach = 0.001
    vault = [-(math.inf),(math.inf)]
    max = 2*math.pi
    min = 0
    while min<max:
        mid = (min+max)/2
        if (mid==min | mid==max):
            break
        curr = func(mid)
        if curr<vault(1) :
           vault(1) = curr
           vault(2) = mid
        if curr<reach :
            max = mid
        else :
            min = mid
