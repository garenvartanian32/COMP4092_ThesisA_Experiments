def provider_of(iface):

    def invariant(value):
        if not iface.providedBy(value):
            raise ValueError(f'Value does not provide the required interface: {iface}')
    return invariant

def validate_with_invariant(value, invariant):
    """Validate a value using the provided invariant."""
    invariant(value)
from zope.interface import Interface, implementer

class IMyInterface(Interface):
    pass

@implementer(IMyInterface)
class MyClass:
    pass
my_instance = MyClass()