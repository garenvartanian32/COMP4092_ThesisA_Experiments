def width_rect_weir(FlowRate, Height):
    #Checking input validity
    ut.check_range([FlowRate, ">0", "Flow rate"], [Height, ">0", "Height"])
    return ((3 / 2) * FlowRate
            / (con.VC_ORIFICE_RATIO * np.sqrt(2 * gravity.magnitude) * Height ** (3 / 2))
            )