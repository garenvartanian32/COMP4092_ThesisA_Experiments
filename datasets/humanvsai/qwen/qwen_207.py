def _compute_weights(self):
    n = self.dim_x
    alpha = self.alpha
    beta = self.beta
    kappa = self.kappa
    lambda_ = alpha ** 2 * (n + kappa) - n
    c = 0.5 / (n + lambda_)
    self.Wm = np.full(n * 2 + 1, c)
    self.Wc = np.full(n * 2 + 1, c)
    self.Wm[0] = lambda_ / (n + lambda_)
    self.Wc[0] = lambda_ / (n + lambda_) + (1 - alpha ** 2 + beta)
    return (self.Wm, self.Wc)