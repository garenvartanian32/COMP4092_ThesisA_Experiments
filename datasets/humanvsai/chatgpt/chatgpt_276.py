import zope.interface

def require_interface(value):
    zope.interface.verify.verifyObject(zope.interface.Interface, value)
