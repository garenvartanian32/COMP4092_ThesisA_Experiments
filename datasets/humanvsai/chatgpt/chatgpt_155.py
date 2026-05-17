import inspect

def no_arg_views():
    """
    Populate this list with all views that take no arguments.
    """
    views_list = []
    for name, obj in inspect.getmembers(module_with_views):
        if inspect.isfunction(obj) and not inspect.getfullargspec(obj).args:
            views_list.append(obj)
    return views_list

# Replace 'module_with_views' with the name of the module where your views are defined
