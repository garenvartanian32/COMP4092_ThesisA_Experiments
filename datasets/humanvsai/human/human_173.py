def _nbaSeason(x):
    if len(str(x)) == 4:
        try:
            return '{0}-{1}'.format(x, str(int(x) % 100 + 1)[-2:].zfill(2))
        except ValueError: 
            raise ValueError("Enter the four digit year for the first half of the desired season")
    else: raise ValueError("Enter the four digit year for the first half of the desired season")