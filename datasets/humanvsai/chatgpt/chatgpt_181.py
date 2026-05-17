import boto3

def create_identity_pool(IdentityPoolName, AllowUnauthenticatedIdentities=False, 
                         AllowClassicFlow=False, SupportedLoginProviders=None, 
                         DeveloperProviderName=None, OpenIdConnectProviderARNs=None):

    cognito_identity = boto3.client('cognito-identity')

    response = cognito_identity.create_identity_pool(
        IdentityPoolName=IdentityPoolName,
        AllowUnauthenticatedIdentities=AllowUnauthenticatedIdentities,
        AllowClassicFlow=AllowClassicFlow,
        SupportedLoginProviders=SupportedLoginProviders,
        DeveloperProviderName=DeveloperProviderName,
        OpenIdConnectProviderARNs=OpenIdConnectProviderARNs
    )
    
    return response
