def get_order_specification_visitor(name, registry=None):
    if registry is None:
        registry = get_utility_registry()
    return registry.get_utility(IOrderSpecificationVisitor, name)

def get_utility_registry():
    """Returns the utility registry."""
    return UtilityRegistry()

class UtilityRegistry:
    """Registry for utilities."""

    def __init__(self):
        self._utilities = {}

    def register_utility(self, interface, name, utility):
        """Registers a utility under the given name for the given interface."""
        if interface not in self._utilities:
            self._utilities[interface] = {}
        self._utilities[interface][name] = utility

    def get_utility(self, interface, name):
        """Returns the utility registered under the given name for the given
        interface."""
        if interface in self._utilities and name in self._utilities[interface]:
            return self._utilities[interface][name]
        return None

class IOrderSpecificationVisitor:
    """Interface for order specification visitors."""
    pass
registry = UtilityRegistry()

class AscendingOrderVisitor(IOrderSpecificationVisitor):
    """Visitor for ascending order."""

    def visit(self, order_specification):
        print('Ascending order:', order_specification)

class DescendingOrderVisitor(IOrderSpecificationVisitor):
    """Visitor for descending order."""

    def visit(self, order_specification):
        print('Descending order:', order_specification)
visitor = get_order_specification_visitor('ascending', registry)