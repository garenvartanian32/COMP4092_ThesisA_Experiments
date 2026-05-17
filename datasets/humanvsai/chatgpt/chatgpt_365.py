def retrieve_plist_value_by_path(path_segments):
    try:
        plist_data = get_plist_data() #function that will retrieve the plist data
        for key in path_segments:
            plist_data = plist_data[key]
        return plist_data
    except (KeyError, TypeError):
        return None
