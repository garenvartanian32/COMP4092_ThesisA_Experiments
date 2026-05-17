def cat_core(list_of_columns, sep):
    list_with_sep = [sep] * (2 * len(list_of_columns) - 1)
    list_with_sep[::2] = list_of_columns
    return np.sum(list_with_sep, axis=0)