def fetch_next_page(previous_page):
    if '_pagination_next' in previous_page:
        # extract the url to fetch next page
        next_page_url = previous_page['_pagination_next']

        # fetch the next page data using the url
        next_page_data = requests.get(next_page_url).json()

        # return the next page data
        return next_page_data
    
    else:
        # no further data is available
        return None
