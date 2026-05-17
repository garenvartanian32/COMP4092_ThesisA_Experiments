def toJArray(gateway, jtype, arr):
    """
    Convert python list to java type array
    :param gateway: Py4j Gateway
    :param jtype: java type of element in array
    :param arr: python type list
    """
    jarr = gateway.new_array(jtype, len(arr))
    for i in range(0, len(arr)):
        jarr[i] = arr[i]
    return jarr