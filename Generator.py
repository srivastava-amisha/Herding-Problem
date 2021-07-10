def Generator(num_agent,obj,P):
    agents = []
    
    for i in range(num_agent):
        agents.append(obj(P))

    return agents
    
