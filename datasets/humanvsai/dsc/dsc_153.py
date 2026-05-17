def findRange(self, excelLib, start, end):
    """return low and high as excel range"""
    low = min(excelLib[start:end])
    high = max(excelLib[start:end])
    return low, high