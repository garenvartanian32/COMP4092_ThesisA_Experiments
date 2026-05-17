def create_identity_pool(IdentityPoolName,
                         AllowUnauthenticatedIdentities=False,
                         SupportedLoginProviders=None,
                         DeveloperProviderName=None,
                         OpenIdConnectProviderARNs=None,
                         region=None, key=None, keyid=None, profile=None):
    SupportedLoginProviders = dict() if SupportedLoginProviders is None else SupportedLoginProviders
    OpenIdConnectProviderARNs = list() if OpenIdConnectProviderARNs is None else OpenIdConnectProviderARNs
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        request_params = dict(IdentityPoolName=IdentityPoolName,
                              AllowUnauthenticatedIdentities=AllowUnauthenticatedIdentities,
                              SupportedLoginProviders=SupportedLoginProviders,
                              OpenIdConnectProviderARNs=OpenIdConnectProviderARNs)
        if DeveloperProviderName:
            request_params['DeveloperProviderName'] = DeveloperProviderName
        response = conn.create_identity_pool(**request_params)
        response.pop('ResponseMetadata', None)
        return {'created': True, 'identity_pool': response}
    except ClientError as e:
        return {'created': False, 'error': __utils__['boto3.get_error'](e)}