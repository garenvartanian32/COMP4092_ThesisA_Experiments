def fetch_next(self, previous_page):
    if not previous_page:
        return None
    pagination_info = previous_page.get('_pagination_next')
    if not pagination_info:
        return None
    url = pagination_info.get('url')
    params = pagination_info.get('params', {})
    if not url:
        return None
    response = self.session.get(url, params=params)
    response.raise_for_status()
    next_page = response.json()
    return next_page