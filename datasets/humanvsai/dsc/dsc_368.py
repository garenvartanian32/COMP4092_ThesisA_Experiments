import re

class MyClass:
    AWS_SNS_BOUNCE_CERT_TRUSTED_DOMAINS = ['amazonaws.com', 'mytrusteddomain.com']

    def _get_cert_url(self, url):
        for domain in self.AWS_SNS_BOUNCE_CERT_TRUSTED_DOMAINS:
            if re.search(r'\b' + domain + r'\b', url):
                return url
        return None