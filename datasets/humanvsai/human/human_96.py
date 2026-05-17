def get_means_and_scales(self):
        return self.optim.parameters[::2], np.exp(self.optim.parameters[1::2])