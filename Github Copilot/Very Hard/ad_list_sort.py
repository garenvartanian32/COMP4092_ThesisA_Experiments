def advanced_sort(lst):
    order = []
    groups = {}
    for item in lst:
        if item not in groups:
            order.append(item)
            groups[item] = []
        groups[item].append(item)
    return [groups[key] for key in order]