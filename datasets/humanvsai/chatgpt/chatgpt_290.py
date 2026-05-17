def and_joined_filter(*filters):
    return {'$and': list(filters)}
