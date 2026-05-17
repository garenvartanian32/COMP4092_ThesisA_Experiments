import scipy.io as sio

def serialize_to_matpower(case, filename):
    """
    Serialize the input power system case to a MATPOWER data file.

    Parameters:
    -----------
    case : dict
        Dictionary containing the power system case data in MATPOWER format.
    filename : str
        Name of the file to which the MATPOWER data is to be saved.

    Returns:
    --------
    None
    """
    
    sio.savemat(filename, {'mpc': case}, appendmat=False, format='4')
