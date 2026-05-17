def sort_dataframe(df, column, key=None, reverse=False):
    df.sort_values(by=column, key=key, inplace=True, ascending=not reverse)
