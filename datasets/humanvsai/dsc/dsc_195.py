def display_trajectory(sys, times, coords_list, box_vectors=None):
    """
    Display the the system *sys* and instrument the trajectory
    viewer with frames information.

    Parameters
    ----------
    sys: System
        The system to be displayed
    times: np.ndarray(NFRAMES, dtype=float)
        The time corresponding to each frame. This is used
        only for feedback reasons.
    coords_list: list of np.ndarray((NFRAMES, 3), dtype=float)
        Atomic coordinates at each frame.
    box_vectors: np.ndarray((NFRAMES, 3, 3), dtype=float), optional
        The box vectors at each frame.
    """
    # Your code here