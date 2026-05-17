def get_valid_subcategories(layer):
    if layer == 'hazard':
        return ['earthquake', 'flood', 'wildfire', 'tornado']
    elif layer == 'exposure':
        return ['buildings', 'roads', 'bridges', 'power lines']
    else:
        return []
