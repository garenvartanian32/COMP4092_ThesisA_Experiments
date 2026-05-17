def pretty_constants(self):
    return [(i, self.pretty_type(c), c.value) for (i, c) in enumerate(self.constant_pool)]

def pretty_type(self, constant):
    """Returns a pretty string representation of the type of the constant."""
    if isinstance(constant, ConstantInteger):
        return 'int'
    elif isinstance(constant, ConstantFloat):
        return 'float'
    elif isinstance(constant, ConstantString):
        return 'string'
    elif isinstance(constant, ConstantClass):
        return 'class'
    elif isinstance(constant, ConstantNameAndType):
        return 'name_and_type'
    elif isinstance(constant, ConstantFieldref):
        return 'fieldref'
    elif isinstance(constant, ConstantMethodref):
        return 'methodref'
    elif isinstance(constant, ConstantInterfaceMethodref):
        return 'interface_methodref'
    elif isinstance(constant, ConstantInvokeDynamic):
        return 'invoke_dynamic'
    elif isinstance(constant, ConstantMethodHandle):
        return 'method_handle'
    elif isinstance(constant, ConstantMethodType):
        return 'method_type'
    elif isinstance(constant, ConstantModule):
        return 'module'
    elif isinstance(constant, ConstantPackage):
        return 'package'
    else:
        return 'unknown'