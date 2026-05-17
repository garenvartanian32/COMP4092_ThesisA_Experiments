def get_source_values(source_list):
    return [source.get('source_from') for source in source_list if source.get('source_from') is not None]
