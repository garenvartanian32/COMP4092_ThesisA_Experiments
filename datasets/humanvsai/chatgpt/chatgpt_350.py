def remove_row(row):
    if row == 1:
        raise TableError("Header cannot be removed.")
    elif row >= len(table_data):
        raise TableError("Attempt to remove nonexistent row.")
    else:
        del table_data[row-1]
