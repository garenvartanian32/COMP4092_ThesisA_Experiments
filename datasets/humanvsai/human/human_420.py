def _get_mean(self, data, dctx, dists):
        # For values outside of the interpolation range use -999. to ensure
        # value is identifiable and outside of potential real values
        interpolator_mean = interp1d(dists, data,
                                     bounds_error=False,
                                     fill_value=-999.)
        mean = interpolator_mean(getattr(dctx, self.distance_type))
        # For those distances less than or equal to the shortest distance
        # extrapolate the shortest distance value
        mean[getattr(dctx, self.distance_type) < (dists[0] + 1.0E-3)] = data[0]
        # For those distances significantly greater than the furthest distance
        # set to 1E-20.
        mean[getattr(dctx, self.distance_type) > (dists[-1] + 1.0E-3)] = 1E-20
        # If any distance is between the final distance and a margin of 0.001
        # km then assign to smallest distance
        mean[mean < -1.] = data[-1]
        return mean