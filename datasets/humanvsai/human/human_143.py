def valid_daily_max_min_temperature(comp, units='K'):
    r"""Decorator to check that a computation runs on valid min and max temperature datasets."""
    @wraps(comp)
    def func(tasmax, tasmin, **kwds):
        valid_daily_max_temperature(tasmax, units)
        valid_daily_min_temperature(tasmin, units)
        return comp(tasmax, tasmin, **kwds)
    return func