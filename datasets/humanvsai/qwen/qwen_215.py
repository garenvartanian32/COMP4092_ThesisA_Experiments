def fix(x, digs):
    if digs <= 0:
        return f'{int(x)}'
    else:
        return f'{x:.{digs}f}'