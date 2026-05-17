def dmtoind(dm, f_min, f_max, nchan0, inttime, it):
    nchan = nchan0 * 2 ** it
    df = (f_max - f_min) / (nchan - 1)
    dm_delay = 4148808.0 * dm / f_min ** 2
    nsamp = int(dm_delay / (inttime * df))
    start_index = max(0, nsamp - nchan + 1)
    end_index = min(nchan, nsamp + 1)
    return (start_index, end_index)
dm = 100
f_min = 1000
f_max = 1500
nchan0 = 128
inttime = 0.001
it = 2
(start_index, end_index) = dmtoind(dm, f_min, f_max, nchan0, inttime, it)