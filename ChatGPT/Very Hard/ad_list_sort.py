def advanced_sort(items):
    groups = []

    for item in items:
        found = False

        for group in groups:
            if group[0] == item:
                group.append(item)
                found = True
                break

        if not found:
            groups.append([item])

    return groups