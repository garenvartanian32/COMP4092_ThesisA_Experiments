import numpy as np

def compute_ukf_weights(n, alpha=0.001, beta=2, kappa=0):
    """
    Computes the weights for the unscented Kalman filter. In this
    formulation the weights for the mean and covariance are the same.

    :param n: The dimension of the state space
    :param alpha: A tunable scaling parameter (default 0.001)
    :param beta: Incorporates prior knowledge of the distribution of the state (default 2)
    :param kappa: Scaling parameter for the distribution (default 0)
    :return: A tuple containing the weight vectors for the mean and covariance calculations
    """
    lambda_ = alpha**2 * (n + kappa) - n
    c = n + lambda_
    w_m = np.full(2 * n + 1, 1 / (2 * c))
    w_cov = np.copy(w_m)
    w_m[0] = lambda_ / c
    w_cov[0] = w_m[0] + (1 - alpha**2 + beta)
    return w_m, w_cov
