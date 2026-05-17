import pandas as pd

def sort_columns(df, column, key=None, reverse=False):
    df.sort_values(by=column, key=key, ascending=not reverse, inplace=True)