def newton(self):
        dae = self.system.dae
        while True:
            inc = self.calc_inc()
            dae.x += inc[:dae.n]
            dae.y += inc[dae.n:dae.n + dae.m]
            self.niter += 1
            max_mis = max(abs(inc))
            self.iter_mis.append(max_mis)
            self._iter_info(self.niter)
            if max_mis < self.config.tol:
                self.solved = True
                break
            elif self.niter > 5 and max_mis > 1000 * self.iter_mis[0]:
                logger.warning('Blown up in {0} iterations.'.format(self.niter))
                break
            if self.niter > self.config.maxit:
                logger.warning('Reached maximum number of iterations.')
                break
        return self.solved, self.niter