def simBirth(self,which_agents):
        # Get and store states for newly born agents
        N = np.sum(which_agents) # Number of new consumers to make
        aNrmNow_new = drawLognormal(N,mu=self.aNrmInitMean,sigma=self.aNrmInitStd,seed=self.RNG.randint(0,2**31-1))
        self.pLvlNow[which_agents] = drawLognormal(N,mu=self.pLvlInitMean,sigma=self.pLvlInitStd,seed=self.RNG.randint(0,2**31-1))
        self.aLvlNow[which_agents] = aNrmNow_new*self.pLvlNow[which_agents]
        self.t_age[which_agents]   = 0 # How many periods since each agent was born
        self.t_cycle[which_agents] = 0