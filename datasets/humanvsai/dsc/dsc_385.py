import importlib

def reload_class(self, verbose=True, reload_module=True):
    """special class reloading function
    This function is often injected as rrr of classes"""

    # Get the class name
    class_name = self.__class__.__name__

    # Get the module name
    module_name = self.__module__

    if verbose:
        print(f"Reloading class: {class_name} from module: {module_name}")

    # Reload the module
    if reload_module:
        importlib.reload(sys.modules[module_name])

    # Get the new class
    new_class = getattr(sys.modules[module_name], class_name)

    # Create a new instance of the class
    new_instance = new_class()

    # Copy the old instance's attributes to the new instance
    new_instance.__dict__ = self.__dict__

    return new_instance