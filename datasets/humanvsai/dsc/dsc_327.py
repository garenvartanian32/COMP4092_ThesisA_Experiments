import math

def width_rect_weir(FlowRate, Height):
    """Return the width of a rectangular weir."""
    return FlowRate / (Height * math.sqrt(Height))