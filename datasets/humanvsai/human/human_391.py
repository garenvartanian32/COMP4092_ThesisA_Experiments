def get_curricula_by_department(
        department, future_terms=0, view_unpublished=False):
    if not isinstance(future_terms, int):
        raise ValueError(future_terms)
    if future_terms < 0 or future_terms > 2:
        raise ValueError(future_terms)
    view_unpublished = "true" if view_unpublished else "false"
    url = "{}?{}".format(
        curriculum_search_url_prefix,
        urlencode([("department_abbreviation", department.label,),
                   ("future_terms", future_terms,),
                   ("view_unpublished", view_unpublished,)]))
    return _json_to_curricula(get_resource(url))