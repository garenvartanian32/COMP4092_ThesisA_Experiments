def worker(func, *args):
    from numba import jit

    @jit(nopython=True)
    def engine():
        func(*args)
    
    engine()
