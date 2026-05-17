def search_archives(query):
    _assert_obj_type(query, name="query", obj_type=DBArchive)
    return _get_handler().search_objects(query)