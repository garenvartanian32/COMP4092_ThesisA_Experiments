def dmtoind(dm, f_min, f_max, nchan0, inttime, it):
    #    maxDT = dmtodt(dm) # need to write
    if it>0:
        correction = dF/2.
    else:
        correction = 0
    shift = []
    nchan = nchan0/2**(iteration_num)
    for i_F in range(nchan):
        f_start = (f_max - f_min)/float(nchan) * (i_F) + f_min
        f_end = (f_max - f_min)/float(nchan) *(i_F+1) + f_min
        f_middle = (f_end - f_start)/2. + f_start - correction
        f_middle_larger = (f_end - f_start)/2 + f_start + correction
        dT_middle = int(round(i_dT * (1./f_middle**2 - 1./f_start**2)/(1./f_end**2 - 1./f_start**2)))
        dT_middle_larger = int(round(i_dT * (1./f_middle_larger**2 - 1./f_start**2)/(1./f_end**2 - 1./f_start**2)))
        shift.append( (-dT_middle_larger, i_F) )