def get_unsafe_name(requirement):
    if requirement['name']:
        return requirement['name']['unsafe']
    else:
        raise ValueError('No name found in requirement')
