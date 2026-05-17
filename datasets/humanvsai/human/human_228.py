def _find_integer_tolerance(epsilon, v_max, min_tol):
    int_tol = min(epsilon / (10 * v_max), 0.1)
    min_tol = max(1e-10, min_tol)
    if int_tol < min_tol:
        eps_lower = min_tol * 10 * v_max
        logger.warning(
            'When the maximum flux is {}, it is recommended that'
            ' epsilon > {} to avoid numerical issues with this'
            ' solver. Results may be incorrect with'
            ' the current settings!'.format(v_max, eps_lower))
        return min_tol
    return int_tol