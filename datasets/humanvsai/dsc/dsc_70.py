def total_flux(self, kwargs_list, norm=False, k=None):
    flux_list = []
    for i, kwargs in enumerate(kwargs_list):
        if k is not None and i != k:
            continue
        if 'amp' in kwargs:
            amp = kwargs['amp']
        elif norm:
            amp = 1
        else:
            amp = 0
        flux = self.compute_flux(kwargs, amp)
        flux_list.append(flux)
    return flux_list