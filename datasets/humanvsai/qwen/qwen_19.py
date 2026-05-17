def get_metric_index(self, data_source):
    if data_source.user_input_index:
        return data_source.user_input_index
    else:
        return data_source.default_index