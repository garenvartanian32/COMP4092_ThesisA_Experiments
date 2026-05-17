import pandas as pd

def make_histogram(data, bins):
    nbins = len(bins) - 1
    binned = pd.DataFrame(index=range(nbins), columns=data.columns)
    
    for column in data.columns:
        binned_column = pd.cut(data[column], bins=bins)
        binned[column] = binned_column.value_counts(sort=False)
    
    return binned
