def _compute_weights(self):
        n = self.n
        k = self.kappa
        self.Wm = np.full(2*n+1, .5 / (n + k))
        self.Wm[0] = k / (n+k)
        self.Wc = self.Wm