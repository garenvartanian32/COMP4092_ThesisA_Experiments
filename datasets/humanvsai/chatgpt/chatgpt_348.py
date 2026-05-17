import importlib

def search_register(function_name: str, registered_functions: dict) -> callable:
    if function_name in registered_functions:
        return registered_functions[function_name]
    else:
        module_name, function_name = function_name.split('.')
        function_module = importlib.import_module(module_name)
        function_to_register = getattr(function_module, function_name)
        registered_functions[function_name] = function_to_register
        return function_to_register
