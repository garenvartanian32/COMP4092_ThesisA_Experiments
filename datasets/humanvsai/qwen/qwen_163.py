def simBirth(self, which_agents):
    new_agents = np.zeros(self.AgentCount, dtype=[('aNrm', 'f4'), ('pLvl', 'f4'), ('t_age', 'i4'), ('t_cycle', 'i4')])
    new_agents['aNrm'] = np.random.lognormal(mean=self.aNrmInitMean, sigma=self.aNrmInitStd, size=self.AgentCount)
    new_agents['pLvl'] = np.random.lognormal(mean=self.pLvlInitMean, sigma=self.pLvlInitStd, size=self.AgentCount)
    new_agents['t_age'] = 0
    new_agents['t_cycle'] = 0
    self.agents[which_agents] = new_agents[which_agents]
    return None