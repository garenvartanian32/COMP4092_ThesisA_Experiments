def _find_integer_tolerance(epsilon, v_max, min_tol):
    """Find appropriate integer tolerance for gap-filling problems."""
    tol = int(epsilon / v_max * 100)
    if tol < min_tol:
        return min_tol
    else:
        return tol