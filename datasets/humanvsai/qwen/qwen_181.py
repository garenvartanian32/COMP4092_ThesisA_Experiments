def create_identity_pool(IdentityPoolName, DeveloperProviderName=None, SupportedLoginProviders=None, OpenIdConnectProviderARNs=None, AllowUnauthenticatedIdentities=False):
    """Creates a new identity pool.  All parameters except for IdentityPoolName is optional.
    SupportedLoginProviders should be a dictionary mapping provider names to provider app
    IDs.  OpenIdConnectProviderARNs should be a list of OpenID Connect provider ARNs.

    Returns the created identity pool if successful

    CLI Example:

    .. code-block:: bash

        salt myminion boto_cognitoidentity.create_identity_pool my_id_pool_name                              DeveloperProviderName=custom_developer_provider"""
    import boto3
    client = boto3.client('cognito-identity')
    response = client.create_identity_pool(IdentityPoolName=IdentityPoolName, AllowUnauthenticatedIdentities=AllowUnauthenticatedIdentities, DeveloperProviderName=DeveloperProviderName, SupportedLoginProviders=SupportedLoginProviders, OpenIdConnectProviderARNs=OpenIdConnectProviderARNs)
    return response