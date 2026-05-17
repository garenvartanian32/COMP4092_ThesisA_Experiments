from zope.interface import Interface, providedBy

class IMyInterface(Interface):
    pass

def provider_of(iface, obj):
    return iface.providedBy(obj)

class MyClass:
    pass

my_obj = MyClass()
print(provider_of(IMyInterface, my_obj))  # prints: False