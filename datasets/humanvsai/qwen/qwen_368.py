def _get_cert_url(self):
    trusted_domains = self.settings.get('AWS_SNS_BOUNCE_CERT_TRUSTED_DOMAINS', [])
    cert_url = self.settings.get('AWS_SNS_BOUNCE_CERT_URL', '')
    if not cert_url:
        return None
    parsed_url = urlparse(cert_url)
    domain = parsed_url.netloc
    for trusted_domain in trusted_domains:
        if domain.endswith(trusted_domain):
            return cert_url
    return None