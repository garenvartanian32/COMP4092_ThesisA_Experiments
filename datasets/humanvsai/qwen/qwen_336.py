def get_output_jsonpath_field(self, sub_output=None):
    if sub_output is None:
        sub_output = self.output
    jsonpath = f'$.{sub_output}'
    return jsonpath

def get_output_jsonpath_field(self, sub_output=None):
    """attempts to create an output jsonpath from a particular output field"""
    if sub_output is None:
        sub_output = self.output
    jsonpath = f'$.{sub_output}'
    return jsonpath