def get_means_and_scales(self):
    means = []
    scales = []
    for param in self.parameters():
        mean = param.data.mean().item()
        scale = param.data.std().item()
        means.append(mean)
        scales.append(scale)
    return (means, scales)