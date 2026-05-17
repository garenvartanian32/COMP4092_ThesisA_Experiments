class MyClass:
    def request_output(self, table, outtype):
        if outtype == 'CSV':
            # code to generate CSV output
            pass
        elif outtype == 'DataSet':
            # code to generate DataSet output
            pass
        elif outtype == 'FITS':
            # code to generate FITS output
            pass
        elif outtype == 'VOTable':
            # code to generate VOTable output
            pass
        else:
            print('Invalid output type')