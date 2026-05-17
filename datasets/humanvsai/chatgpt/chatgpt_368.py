def get_signing_cert_url(url: str, trusted_domains: list) -> str:
    parsed_url = urlparse(url)
    allowed_domains = [td if td.startswith('.') else '.' + td for td in trusted_domains]
    for domain in allowed_domains:
        if parsed_url.hostname.endswith(domain):
            return url
        
    raise ValueError(f"{url} is not a valid trusted url")
