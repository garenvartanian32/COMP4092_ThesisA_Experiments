def build(self, track_list=None, min_length=0, adjust_dynamics=False):
    """
    Create a numpy array from the composition.

    :param track_list: List of tracks to include in composition generation (``None`` means all tracks will be used)
    :type track_list: list of :py:class:`radiotool.composer.Track`
    :param int min_length: Minimum length of output array (in frames). Will zero pad extra length.
    :param bool adjust_dynamics: Automatically adjust dynamics. Will document later.
    """
    # Your function implementation goes here