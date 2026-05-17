def subcategories_for_layer(self, layer):
    """Return a list of valid subcategories for a layer.
           Subcategory is hazard type or exposure type.

        :param layer: The layer for which to return valid subcategories.
        :type layer: str
        :returns: A list where each value represents a valid subcategory.
        :rtype: list"""

    # Assuming you have a dictionary where keys are layers and values are lists of valid subcategories
    valid_subcategories = {
        'layer1': ['subcategory1', 'subcategory2'],
        'layer2': ['subcategory3', 'subcategory4'],
        # Add more layers and their valid subcategories as needed
    }

    return valid_subcategories.get(layer, [])