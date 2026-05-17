def cat_core(list_of_columns, sep):
    import numpy as np
    concatenated_strings = []
    for i in range(len(list_of_columns[0])):
        row_strings = []
        for column in list_of_columns:
            row_strings.append(str(column[i]))
        concatenated_strings.append(sep.join(row_strings))
    result = np.array(concatenated_strings)
    return result