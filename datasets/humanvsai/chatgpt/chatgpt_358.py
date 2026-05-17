def compute_jacobian(maps):
    a = maps['a']
    b = maps['b']
    x = maps['x']
    jacobian = (b-a)/((x-a)*(b-x))
    return jacobian