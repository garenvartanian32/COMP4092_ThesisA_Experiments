def _argsdicts(args, mydict):
    """A utility generator that pads argument list and dictionary values, will only be called with len(args) = 0, 1."""
    # Pad the arguments list
    while len(args) < 2:
        args.append(None)

    # Pad the dictionary values
    for key in mydict:
        while len(mydict[key]) < 2:
            mydict[key].append(None)

    yield args, mydict