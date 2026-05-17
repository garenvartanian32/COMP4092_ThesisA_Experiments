import pandas as pd

def export_table(table, outtype):
    if outtype == 'CSV':
        df = pd.read_csv(f'{table}.csv')
        return df.to_csv(index=False)
    elif outtype == 'DataSet':
        df = pd.read_csv(f'{table}.csv')
        return df.to_xml()
    elif outtype == 'FITS':
        # code to export table to FITS format
        pass
    elif outtype == 'VOTable':
        # code to export table to VOTable format
        pass
    else:
        return f"Invalid output type '{outtype}'"
