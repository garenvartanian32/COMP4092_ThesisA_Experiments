from typing import List, Tuple

def query_view(view: List[Tuple], fields: List[str]) -> List[Tuple]:
    """
    Query the given fields of items in the given view.
    The result list contains named tuples,
    so you can access the fields directly by their name.
    """
    result = []
    for item in view:
        named_tuple = {}
        for field in fields:
            named_tuple[field] = item[fields.index(field)]
        result.append(namedtuple('Result', named_tuple.keys())(*named_tuple.values()))
    return result
