def multicall(self, viewname, fields):
    result = []
    for item in self.view(viewname):
        item_data = {field: item[field] for field in fields}
        result.append(item_data)
    return result