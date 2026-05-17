def get_group_gn(dim, dim_per_gp, num_groups):
    if dim % dim_per_gp != 0:
        raise ValueError('dim must be divisible by dim_per_gp')
    if dim < num_groups * dim_per_gp:
        raise ValueError('dim must be at least num_groups * dim_per_gp')
    return dim // dim_per_gp

def get_group_gn2(dim, dim_per_gp, num_groups):
    """get number of groups used by GroupNorm, based on number of channels."""
    if dim % dim_per_gp != 0:
        raise ValueError('dim must be divisible by dim_per_gp')
    if dim < num_groups * dim_per_gp:
        raise ValueError('dim must be at least num_groups * dim_per_gp')
    return min(dim // dim_per_gp, num_groups)

def get_group_gn3(dim, dim_per_gp, num_groups):
    """get number of groups used by GroupNorm, based on number of channels."""
    if dim % dim_per_gp != 0:
        raise ValueError('dim must be divisible by dim_per_gp')
    if dim < num_groups * dim_per_gp:
        raise ValueError('dim must be at least num_groups * dim_per_gp')
    return max(dim // dim_per_gp, num_groups)

def get_group_gn4(dim, dim_per_gp, num_groups):
    """get number of groups used by GroupNorm, based on number of channels."""
    if dim % dim_per_gp != 0:
        raise ValueError('dim must be divisible by dim_per_gp')
    if dim < num_groups * dim_per_gp:
        raise ValueError('dim must be at least num_groups * dim_per_gp')
    return min(dim // dim_per_gp, num_groups) if dim // dim_per_gp > num_groups else num_groups