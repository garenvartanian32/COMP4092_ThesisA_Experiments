def get_access_information(self, code, update_session=False):
    """
    Return the access information for an OAuth2 authorization grant.

    :param code: the code received in the request from the OAuth2 server
    :param update_session: Update the current session with the retrieved
        token(s). Defaults to False.
    :returns: A dictionary with the key/value pairs for access_token,
        refresh_token and scope. The refresh_token value will be done when
        the OAuth2 grant is not refreshable.
    """
    # Your code here