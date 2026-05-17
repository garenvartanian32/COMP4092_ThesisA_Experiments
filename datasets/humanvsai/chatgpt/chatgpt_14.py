import pickle

def get_pickle_hash(pyobj):
    """
    Function that uses the default hash method to return a hash value of a piece of Python
    picklable object.
    :param pyobj: any picklable Python object
    :return: hash value of the pickled object
    """
    pickled_obj = pickle.dumps(pyobj, protocol=pickle.HIGHEST_PROTOCOL)
    return hash(pickled_obj)
