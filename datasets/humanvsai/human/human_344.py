def build_swagger_spec(user, repo, sha, serverName):
    if user and repo:
        # Init provenance recording
        prov_g = grlcPROV(user, repo)
    else:
        prov_g = None
    swag = swagger.get_blank_spec()
    swag['host'] = serverName
    try:
        loader = getLoader(user, repo, sha, prov_g)
    except Exception as e:
        # If repo does not exits
        swag['info'] = {
            'title': 'ERROR!',
            'description': str(e)
        }
        swag['paths'] = {}
        return swag
    prev_commit, next_commit, info, basePath = \
        swagger.get_repo_info(loader, sha, prov_g)
    swag['prev_commit'] = prev_commit
    swag['next_commit'] = next_commit
    swag['info'] = info
    swag['basePath'] = basePath
    # TODO: can we pass loader to build_spec ?
    spec = swagger.build_spec(user, repo, sha, prov_g)
    for item in spec:
        swag['paths'][item['call_name']] = swagger.get_path_for_item(item)
    if prov_g:
        prov_g.end_prov_graph()
        swag['prov'] = prov_g.serialize(format='turtle')
    return swag