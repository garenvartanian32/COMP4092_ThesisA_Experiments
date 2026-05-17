def get_sitej(self, site_index, image_index):
    """Assuming there is some value in the connectivity array at indices
        (1, 3, 12). sitei can be obtained directly from the input structure
        (structure[1]). sitej can be obtained by passing 3, 12 to this function

        Args:
            site_index (int): index of the site (3 in the example)
            image_index (int): index of the image (12 in the example)"""

    # Assuming the connectivity array is a 3D array
    # and the structure is a list of lists
    # and the structure[1] is the sitei

    # Get the sitei from the structure
    sitei = self.structure[1]

    # Get the sitej from the connectivity array
    sitej = self.connectivity_array[1][site_index][image_index]

    return sitej