def call_common_method(plugin_list, method_name, *args):
    for plugin in plugin_list:
        if hasattr(plugin, method_name) and callable(getattr(plugin, method_name)):
            getattr(plugin, method_name)(*args)
