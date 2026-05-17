def normal_h2(size: int = 10000) -> Histogram2D:
    data1 = np.random.normal(0, 1, (size,))
    data2 = np.random.normal(0, 1, (size,))
    return h2(data1, data2, name="normal", axis_names=tuple("xy"), title="2D normal distribution")