def _find_integer_tolerance(epsilon, v_max, min_tol):
    int_tol = int(epsilon * v_max)
    int_tol = max(int_tol, min_tol)
    return int_tol

def _find_float_tolerance(epsilon, v_max, min_tol):
    """Find appropriate float tolerance for gap-filling problems."""
    float_tol = epsilon * v_max
    float_tol = max(float_tol, min_tol)
    return float_tol

def find_tolerance(epsilon, v_max, min_tol, tol_type='integer'):
    """Find appropriate tolerance for gap-filling problems based on the type."""
    if tol_type == 'integer':
        return _find_integer_tolerance(epsilon, v_max, min_tol)
    elif tol_type == 'float':
        return _find_float_tolerance(epsilon, v_max, min_tol)
    else:
        raise ValueError("Invalid tolerance type. Use 'integer' or 'float'.")
epsilon = 0.01
v_max = 100
min_tol = 1
tolerance = find_tolerance(epsilon, v_max, min_tol, tol_type='integer')
tolerance = find_tolerance(epsilon, v_max, min_tol, tol_type='float')