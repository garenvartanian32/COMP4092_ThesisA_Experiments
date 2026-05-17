def get_metric_index(self, data_source):
    # Assuming you have a dictionary where you store the default and user-inputed indices
    indices = {
        'default': 'default_index',
        'user_input': 'user_input_index'
    }

    # If the data source is in the indices dictionary, return the corresponding index
    if data_source in indices:
        return indices[data_source]
    else:
        # If the data source is not in the indices dictionary, return the default index
        return indices['default']