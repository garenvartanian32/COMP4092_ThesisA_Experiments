def flatten(arr):
    flat_arr = []
    for i in arr:
        if isinstance(i, list):
            flat_arr += flatten(i)
        else:
            flat_arr.append(i)
    return flat_arr
