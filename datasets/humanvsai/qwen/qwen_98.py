def build(self, track_list=None, adjust_dynamics=False):

    def __init__(self, track_list=None, adjust_dynamics=False):
        self.track_list = track_list if track_list is not None else []
        self.adjust_dynamics = adjust_dynamics

    def build(self, track_list=None, adjust_dynamics=False, min_length=None):
        """Create a numpy array from the composition.

        :param track_list: List of tracks to include in composition generation (``None`` means all tracks will be used)
        :type track_list: list of :py:class:`radiotool.composer.Track`
        :param int min_length: Minimum length of output array (in frames). Will zero pad extra length.
        :param bool adjust_dynamics: Automatically adjust dynamics. Will document later.
        """
        import numpy as np
        if track_list is None:
            track_list = self.track_list
        track_arrays = []
        for track in track_list:
            track_arrays.append(track.to_array())
        composition_array = np.concatenate(track_arrays, axis=0)
        if min_length is not None and composition_array.shape[0] < min_length:
            composition_array = np.pad(composition_array, (0, min_length - composition_array.shape[0]), 'constant')
        if adjust_dynamics:
            composition_array = self.adjust_dynamics(composition_array)
        return composition_array