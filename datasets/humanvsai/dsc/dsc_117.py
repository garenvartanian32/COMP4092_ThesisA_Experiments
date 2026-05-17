from everest.interfaces import IOrderSpecificationVisitor

def get_order_specification_visitor(name, registry=None):
    """Returns the class registered as the order specification
    visitor utility under the given name (one of the
    :const:`everest.querying.base.EXPRESSION_KINDS` constants).

    :returns: class implementing
        :class:`everest.interfaces.IOrderSpecificationVisitor`"""

    # Assuming you have a dictionary that maps names to classes
    # Replace this with your actual implementation
    class_registry = {
        'name1': Class1,
        'name2': Class2,
        # ...
    }

    if registry is not None:
        class_registry = registry

    try:
        visitor_class = class_registry[name]
    except KeyError:
        raise ValueError(f"No visitor class found for name {name}")

    if not issubclass(visitor_class, IOrderSpecificationVisitor):
        raise TypeError(f"Class {visitor_class} does not implement IOrderSpecificationVisitor")

    return visitor_class