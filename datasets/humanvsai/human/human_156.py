def fetch_next(self, previous_page):
        if isinstance(previous_page, list) and len(previous_page) != 0:
            if hasattr(previous_page[-1], '_pagination_next'):
                params = copy.deepcopy(previous_page[-1]._pagination_next)
            else:
                return None
        else:
            params = copy.deepcopy(previous_page)
        method = params['_pagination_method']
        del params['_pagination_method']
        endpoint = params['_pagination_endpoint']
        del params['_pagination_endpoint']
        return self.__api_request(method, endpoint, params)