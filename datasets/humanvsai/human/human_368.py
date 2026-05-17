def _get_cert_url(self):
        cert_url = self._data.get('SigningCertURL')
        if cert_url:
            if cert_url.startswith('https://'):
                url_obj = urlparse(cert_url)
                for trusted_domain in settings.BOUNCE_CERT_DOMAINS:
                    parts = trusted_domain.split('.')
                    if url_obj.netloc.split('.')[-len(parts):] == parts:
                        return cert_url
            logger.warning(u'Untrusted certificate URL: "%s"', cert_url)
        else:
            logger.warning(u'No signing certificate URL: "%s"', cert_url)
        return None