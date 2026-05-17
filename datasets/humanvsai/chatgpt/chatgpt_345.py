def apply_attributes(codec=None, attrs=None, obj=None):
    """
    Applies the collection of attributes C{attrs} to aliased object C{obj}.
    Called when decoding reading aliased objects from an AMF byte stream.
    Override this to provide fine grain control of application of
    attributes to C{obj}.
    @param codec: An optional argument that will contain the en/decoder
        instance calling this function.
    """
    if attrs is None or obj is None:
        return
    
    for attr in attrs:
        setattr(obj, attr, attrs[attr])
