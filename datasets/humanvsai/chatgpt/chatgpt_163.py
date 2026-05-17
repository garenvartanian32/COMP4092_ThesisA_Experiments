import numpy as np

def make_new_consumers(which_agents):
    aNrmInitMean = 1.0
    aNrmInitStd = 0.0
    pLvlInitMean = 1.0
    pLvlInitStd = 0.0
    t_age_init = 0
        
    # drawing initial aNrm and pLvl for new consumers
    aNrm = np.zeros(np.sum(which_agents))
    pLvl = np.zeros(np.sum(which_agents))

    for i in range(np.sum(which_agents)):
        # draw initial normalized assets
        aNrm[i] = np.exp(np.random.normal(np.log(aNrmInitMean), aNrmInitStd)) 
        # draw initial permanent income level
        pLvl[i] = np.exp(np.random.normal(np.log(pLvlInitMean), pLvlInitStd)) 

    # time variables
    t_age = np.full(np.sum(which_agents), t_age_init)
    t_cycle = np.mod(t_age, self.PeriodsPerCycle)

    return None
