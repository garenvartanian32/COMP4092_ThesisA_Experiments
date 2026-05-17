def get_id_or_json(request, in_batch):
    if in_batch:
        return request['id']
    else:
        return request
