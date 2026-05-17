def viewBoxAxisRange(viewBox, axisNumber):
    rect = viewBox.childrenBoundingRect() # taken from viewBox.autoRange()
    if rect is not None:
        if axisNumber == X_AXIS:
            return rect.left(), rect.right()
        elif axisNumber == Y_AXIS:
            return rect.bottom(), rect.top()
        else:
            raise ValueError("axisNumber should be 0 or 1, got: {}".format(axisNumber))
    else:
        # Does this happen? Probably when the plot is empty.
        raise AssertionError("No children bbox. Plot range not updated.")