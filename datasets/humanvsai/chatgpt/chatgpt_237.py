def get_trigger_strings(item):
    triggers = []  # create a list to hold the trigger strings
    
    # check if item has any triggers
    if item in ITEM_TRIGGERS:
        triggers = ITEM_TRIGGERS[item]  # assign the triggers to the list
    
    # return the triggers as a tuple if any exist, otherwise return None
    return tuple(triggers) if triggers else None
