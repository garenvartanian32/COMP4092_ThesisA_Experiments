import jsonpath

def create_output_jsonpath(output_field):
    """
    Attempts to create an output jsonpath from a particular output field
    """

    # Create a base jsonpath based on the output field name
    base_jsonpath = "$." + output_field

    # Attempt to parse the base jsonpath and return it
    try:
        jsonpath.JsonPath.parse(base_jsonpath)
        return base_jsonpath
    except Exception as e:
        print(f"Error creating jsonpath: {str(e)}")
        return None
