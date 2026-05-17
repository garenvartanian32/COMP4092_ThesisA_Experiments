import boto3

def create_identity_pool(IdentityPoolName, **kwargs):
    client = boto3.client('cognito-identity')

    response = client.create_identity_pool(
        IdentityPoolName=IdentityPoolName,
        AllowUnauthenticatedIdentities=kwargs.get('AllowUnauthenticatedIdentities', False),
        CognitoIdentityProviders=kwargs.get('CognitoIdentityProviders', {}),
        DeveloperProviderName=kwargs.get('DeveloperProviderName', ''),
        OpenIdConnectProviderARNs=kwargs.get('OpenIdConnectProviderARNs', []),
        SamlProviderARNs=kwargs.get('SamlProviderARNs', []),
        SupportedLoginProviders=kwargs.get('SupportedLoginProviders', {})
    )

    return response