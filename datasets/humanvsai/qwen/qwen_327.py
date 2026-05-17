def width_rect_weir(FlowRate, Height):
    g = 9.81
    width = (FlowRate / (2 * g * Height ** (3 / 2))) ** (2 / 3)
    return width
FlowRate = 0.5
Height = 0.2
width = width_rect_weir(FlowRate, Height)