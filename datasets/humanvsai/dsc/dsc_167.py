def get_group_gn(dim, dim_per_gp, num_groups):
    """get number of groups used by GroupNorm, based on number of channels."""
    if dim % dim_per_gp == 0:
        return num_groups
    else:
        return num_groups + 1