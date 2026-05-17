def newton(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton power flow routine

    Parameters
    ----------
    f : function
        Function to solve.
    df : function
        Derivative of f.
    x0 : float
        Initial guess.
    tol : float, optional
        Tolerance for convergence.
    max_iter : int, optional
        Maximum number of iterations.

    Returns
    -------
    (bool, int)
        success flag, number of iterations
    """
    x = x0
    for i in range(max_iter):
        dx = f(x) / df(x)
        x -= dx
        if abs(dx) < tol:
            return True, i+1
    return False, max_iter