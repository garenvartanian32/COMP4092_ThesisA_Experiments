from collections import namedtuple

def multicall(self, viewname, fields):
    # Assuming you have a function to query the view
    results = self.query_view(viewname)

    # Create a named tuple type
    Result = namedtuple('Result', fields)

    # Convert the results to named tuples
    named_results = [Result(**result) for result in results]

    return named_results