def newton(self):
    V = self.V
    S = self.S
    Y = self.Y
    N = len(V)
    V_new = V.copy()
    max_iter = 100
    tol = 1e-06
    iter_count = 0
    while iter_count < max_iter:
        P_mismatch = np.real(S) - np.real(V_new.conj() * (Y @ V_new))
        Q_mismatch = np.imag(S) - np.imag(V_new.conj() * (Y @ V_new))
        mismatch = np.concatenate((P_mismatch, Q_mismatch))
        if np.linalg.norm(mismatch) < tol:
            return (True, iter_count)
        J = np.zeros((2 * N, 2 * N), dtype=complex)
        for i in range(N):
            for j in range(N):
                if i == j:
                    J[i, j] = V_new[i].real * (Y[i, i].imag + 2 * np.imag(Y[i, :].conj() @ V_new))
                    J[i, j + N] = -V_new[i].imag * (Y[i, i].imag + 2 * np.imag(Y[i, :].conj() @ V_new))
                    J[i + N, j] = V_new[i].imag * (Y[i, i].real + 2 * np.real(Y[i, :].conj() @ V_new))
                    J[i + N, j + N] = V_new[i].real * (Y[i, i].real + 2 * np.real(Y[i, :].conj() @ V_new))
                else:
                    J[i, j] = V_new[j].real * Y[i, j].imag - V_new[j].imag * Y[i, j].real