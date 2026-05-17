import chemlab

def display_trajectory(sys: chemlab.core.System, times: np.ndarray, coords_list: List[np.ndarray]) -> None:
    """
    Display the the system sys and instrument the trajectory
    viewer with frames information.

    Parameters
    ----------
    sys: chemlab.core.System
        The system to be displayed
    times: np.ndarray(NFRAMES, dtype=float)
        The time corresponding to each frame. This is used
        only for feedback reasons.
    coords_list: list of np.ndarray((NFRAMES, 3), dtype=float)
        Atomic coordinates at each frame.
    """
    pass
