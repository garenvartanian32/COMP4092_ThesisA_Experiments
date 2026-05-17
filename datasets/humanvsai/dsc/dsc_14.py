import pickle
import hashlib

def of_pyobj(pyobj):
    """Use default hash method to return hash value of a piece of Python
        picklable object.

        :param pyobj: any python object"""
    # Pickle the object
    pickled_obj = pickle.dumps(pyobj)

    # Create a new SHA256 hash object
    hash_obj = hashlib.sha256()

    # Update the hash object with the pickled object
    hash_obj.update(pickled_obj)

    # Return the hexadecimal representation of the hash
    return hash_obj.hexdigest()