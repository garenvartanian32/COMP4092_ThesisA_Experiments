def _compute_weights(self, n):
    """Computes the weights for the unscented Kalman filter. In this
    formulation the weights for the mean and covariance are the same."""
    lambda_ = self.alpha**2 * (n + self.kappa) - n
    weights = np.full(2*n+1, 1/(2*(n + lambda_)))
    weights[0] = lambda_/(n + lambda_)
    return weights