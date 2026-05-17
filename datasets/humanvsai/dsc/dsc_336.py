import jsonpath_rw

class MyClass:
    def __init__(self, data):
        self.data = data

    def get_output_jsonpath_field(self, field):
        jsonpath_expr = jsonpath_rw.parse('$..' + field)
        return [match.value for match in jsonpath_expr.find(self.data)]