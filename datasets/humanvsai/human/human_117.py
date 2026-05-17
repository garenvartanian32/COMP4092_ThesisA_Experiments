def get_order_specification_visitor(name, registry=None):
    if registry is None:
        registry = get_current_registry()
    return registry.getUtility(IOrderSpecificationVisitor, name=name)