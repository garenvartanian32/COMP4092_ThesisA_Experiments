def total_flux(self, kwargs_list, norm=False, k=None):
        norm_flux_list = []
        for i, model in enumerate(self.profile_type_list):
            if k is None or k == i:
                if model in ['SERSIC', 'SERSIC_ELLIPSE', 'INTERPOL', 'GAUSSIAN', 'GAUSSIAN_ELLIPSE',
                             'MULTI_GAUSSIAN', 'MULTI_GAUSSIAN_ELLIPSE']:
                    kwargs_new = kwargs_list[i].copy()
                    if norm is True:
                        if model in ['MULTI_GAUSSIAN', 'MULTI_GAUSSIAN_ELLIPSE']:
                            new = {'amp': np.array(kwargs_new['amp'])/kwargs_new['amp'][0]}
                        else:
                            new = {'amp': 1}
                        kwargs_new.update(new)
                    norm_flux = self.func_list[i].total_flux(**kwargs_new)
                    norm_flux_list.append(norm_flux)
                else:
                    raise ValueError("profile %s does not support flux normlization." % model)
                #  TODO implement total flux for e.g. 'HERNQUIST', 'HERNQUIST_ELLIPSE', 'PJAFFE', 'PJAFFE_ELLIPSE',
                    # 'GAUSSIAN', 'GAUSSIAN_ELLIPSE', 'POWER_LAW', 'NIE', 'CHAMELEON', 'DOUBLE_CHAMELEON', 'UNIFORM'
        return norm_flux_list