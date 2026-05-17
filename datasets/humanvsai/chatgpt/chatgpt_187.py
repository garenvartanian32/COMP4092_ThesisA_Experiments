import asyncio
import functools

def convert_yielded(yld):
    if isinstance(yld, list) or isinstance(yld, dict) or isinstance(yld, asyncio.Future):
        # default implementation
        return asyncio.ensure_future(yld)
    elif hasattr(functools, 'singledispatch'):
        # use singledispatch to extend to additional types
        @convert_yielded.register(# additional type)
        def _(additional_type):
            # additional type conversion code
            return additional_type_conversion_result
    
    else:
        raise TypeError('Unsupported yield type: {}'.format(type(yld)))
