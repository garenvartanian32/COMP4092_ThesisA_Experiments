def _read_points(self, vlrs):
    """private function to handle reading of the points record parts
    of the las file.

    the header is needed for the point format and number of points
    the vlrs are need to get the potential laszip vlr as well as the extra bytes vlr"""
    # Your code here