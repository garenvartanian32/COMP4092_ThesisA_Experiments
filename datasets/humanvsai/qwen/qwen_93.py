def _merge_headers(self, call_specific_headers):
    merged_headers = CaseInsensitiveDict()
    if self.headers:
        merged_headers.update(self.headers)
    if call_specific_headers:
        merged_headers.update(call_specific_headers)
    return merged_headers