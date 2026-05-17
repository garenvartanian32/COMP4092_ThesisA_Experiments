def convert_response(allocate_quota_response, project_id):
    if not allocate_quota_response or not allocate_quota_response.allocateErrors:
        return _IS_OK
    # only allocate_quota the first error for now, as per ESP
    theError = allocate_quota_response.allocateErrors[0]
    error_tuple = _QUOTA_ERROR_CONVERSION.get(theError.code, _IS_UNKNOWN)
    if error_tuple[1].find(u'{') == -1:  # no replacements needed:
        return error_tuple
    updated_msg = error_tuple[1].format(project_id=project_id, detail=theError.description or u'')
    return error_tuple[0], updated_msg