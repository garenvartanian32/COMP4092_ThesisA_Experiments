def compute_total_flux(kwargs_list, norm=False, k=None):
    flux_list = []
    for i, kwargs in enumerate(kwargs_list):
        if k is None or k == i:
            if 'amp' not in kwargs or norm:
                kwargs['amp'] = 1
            flux = kwargs['amp'] * kwargs.get('flux_e', 1) * kwargs.get('sigma_temp', 1) **2
            flux_list.append(flux)
    return flux_list