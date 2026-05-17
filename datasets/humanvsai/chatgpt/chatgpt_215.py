def format_x(x: float, digs: int) -> str:
    if digs <= 0:
        return '{:.0f}'.format(x)
    else:
        return '{:.{}f}'.format(x, digs).rstrip('0').rstrip('.')
