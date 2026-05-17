def viewBoxAxisRange(viewBox, axisNumber):
    if axisNumber == 0:
        return viewBox[2] - viewBox[0]
    elif axisNumber == 1:
        return viewBox[3] - viewBox[1]
    else:
        raise ValueError('axisNumber must be 0 or 1')
viewBox = [0, 0, 100, 100]