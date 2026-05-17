def rename_script(rename=None):  # noqa: E501
    if connexion.request.is_json:
        rename = Rename.from_dict(connexion.request.get_json())  # noqa: E501
    if(not hasAccess()):
        return redirectUnauthorized()
    driver = LoadedDrivers.getDefaultDriver()
    if (not driver.renameScript(rename.original.name, rename.new.name)):
        return ErrorResponse(status=500, message='Cannot rename to an existing file.')
    return Response(status=200, body={'file-name': rename.new.name})