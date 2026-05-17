def pypi_metadata_extension(extraction_fce):
    def inner(self, client=None):
        data = extraction_fce(self)
        if client is None:
            logger.warning("Client is None, it was probably disabled")
            data.update_attr('source0', self.archive.name)
            return data
        try:
            release_data = client.release_data(self.name, self.version)
        except BaseException:
            logger.warning("Some kind of error while communicating with "
                           "client: {0}.".format(client), exc_info=True)
            return data
        try:
            url, md5_digest = get_url(client, self.name, self.version)
        except exc.MissingUrlException:
            url, md5_digest = ('FAILED TO EXTRACT FROM PYPI',
                               'FAILED TO EXTRACT FROM PYPI')
        data_dict = {'source0': url, 'md5': md5_digest}
        for data_field in settings.PYPI_USABLE_DATA:
            data_dict[data_field] = release_data.get(data_field, '')
        # we usually get better license representation from trove classifiers
        data_dict["license"] = license_from_trove(release_data.get(
            'classifiers', ''))
        data.set_from(data_dict, update=True)
        return data
    return inner