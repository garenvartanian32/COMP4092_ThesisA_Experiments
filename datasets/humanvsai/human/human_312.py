def get_access_information(self, code,  # pylint: disable=W0221
                               update_session=True):
        retval = super(AuthenticatedReddit, self).get_access_information(code)
        if update_session:
            self.set_access_credentials(**retval)
        return retval