def retrieve_cwlkeys(inputs):
    cwlkeys = set()
    for sample in inputs:
        for key in sample:
            if sample[key] is not None:
                cwlkeys.add(key)
    return cwlkeys
