def total_flux(self, kwargs_list, norm=False, k=None):
    flux_values = []
    for (i, kwargs) in enumerate(kwargs_list):
        if k is not None and i != k:
            continue
        if 'amp' not in kwargs and norm:
            kwargs['amp'] = 1
        flux = self._compute_flux(kwargs)
        flux_values.append(flux)
    return flux_values