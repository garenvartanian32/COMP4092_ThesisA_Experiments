def reload_class(self, verbose=True, reload_module=True):
    if reload_module:
        import importlib
        importlib.reload(self.__class__.__module__)
    if verbose:
        print(f'Reloaded class {self.__class__.__name__} from module {self.__class__.__module__}')