import re

def search_domains(pattern, domains_list):
    matched_domains = []
    for domain in domains_list:
        if re.search(pattern, domain):
            matched_domains.append(domain)
    return matched_domains
