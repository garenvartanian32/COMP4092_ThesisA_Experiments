def _index_entities(self):
    # Assuming self.index is a list of dictionaries
    # and self.entities is a dictionary
    if not self.index:
        return

    # Get the first dictionary in the index
    common_dict = self.index[0]

    # Iterate over the rest of the dictionaries
    for d in self.index[1:]:
        # Create a new dictionary that only includes keys that are in both dictionaries
        common_dict = {k: common_dict[k] for k in common_dict if k in d and common_dict[k] == d[k]}

    # Set the entities of the current instance to the common keys and values
    self.entities = common_dict