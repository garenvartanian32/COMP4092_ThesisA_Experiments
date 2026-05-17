def classify_gadgets(gadgets):
    """
    Classify binary-operation gadgets.

    Parameters:
    gadgets (list): A list of binary-operation gadgets.

    Returns:
    dict: A dictionary containing the number of occurrences of each type of operation.
    """
    
    counts = {'Add': 0, 'Sub': 0, 'Mul': 0, 'Div': 0, 'Mod': 0, 'Pow': 0, 'And': 0, 'Or': 0, 'Xor': 0, 'Shl': 0, 'Shr': 0}
    
    for gadget in gadgets:
        if 'add' in gadget.lower():
            counts['Add'] += 1
        elif 'sub' in gadget.lower():
            counts['Sub'] += 1
        elif 'mul' in gadget.lower():
            counts['Mul'] += 1
        elif 'div' in gadget.lower():
            counts['Div'] += 1
        elif 'mod' in gadget.lower():
            counts['Mod'] += 1
        elif 'pow' in gadget.lower():
            counts['Pow'] += 1
        elif 'and' in gadget.lower():
            counts['And'] += 1
        elif 'or' in gadget.lower():
            counts['Or'] += 1
        elif 'xor' in gadget.lower():
            counts['Xor'] += 1
        elif 'shl' in gadget.lower():
            counts['Shl'] += 1
        elif 'shr' in gadget.lower():
            counts['Shr'] += 1
    
    return counts
