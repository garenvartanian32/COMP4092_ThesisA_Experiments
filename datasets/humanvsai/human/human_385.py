def reload_class(self, verbose=True, reload_module=True):
    import utool as ut
    verbose = verbose or VERBOSE_CLASS
    classname = self.__class__.__name__
    try:
        modname = self.__class__.__module__
        if verbose:
            print('[class] reloading ' + classname + ' from ' + modname)
        # --HACK--
        if hasattr(self, '_on_reload'):
            if verbose > 1:
                print('[class] calling _on_reload for ' + classname)
            self._on_reload()
        elif verbose > 1:
            print('[class] ' + classname + ' does not have an _on_reload function')
        # Do for all inheriting classes
        def find_base_clases(_class, find_base_clases=None):
            class_list = []
            for _baseclass in _class.__bases__:
                parents = find_base_clases(_baseclass, find_base_clases)
                class_list.extend(parents)
            if _class is not object:
                class_list.append(_class)
            return class_list
        head_class = self.__class__
        # Determine if parents need reloading
        class_list = find_base_clases(head_class, find_base_clases)
        # HACK
        ignore = {HashComparable2}
        class_list = [_class for _class in class_list
                      if _class not in ignore]
        for _class in class_list:
            if verbose:
                print('[class] reloading parent ' + _class.__name__ +
                      ' from ' + _class.__module__)
            if _class.__module__ == '__main__':
                # Attempt to find the module that is the main module
                # This may be very hacky and potentially break
                main_module_ = sys.modules[_class.__module__]
                main_modname = ut.get_modname_from_modpath(main_module_.__file__)
                module_ = sys.modules[main_modname]
            else:
                module_ = sys.modules[_class.__module__]
            if hasattr(module_, 'rrr'):
                if reload_module:
                    module_.rrr(verbose=verbose)
            else:
                if reload_module:
                    import imp
                    if verbose:
                        print('[class] reloading ' + _class.__module__ + ' with imp')
                    try:
                        imp.reload(module_)
                    except (ImportError, AttributeError):
                        print('[class] fallback reloading ' + _class.__module__ +
                              ' with imp')
                        # one last thing to try. probably used ut.import_module_from_fpath
                        # when importing this module
                        imp.load_source(module_.__name__, module_.__file__)
            # Reset class attributes
            _newclass = getattr(module_, _class.__name__)
            reload_class_methods(self, _newclass, verbose=verbose)
        # --HACK--
        # TODO: handle injected definitions
        if hasattr(self, '_initialize_self'):
            if verbose > 1:
                print('[class] calling _initialize_self for ' + classname)
            self._initialize_self()
        elif verbose > 1:
            print('[class] ' + classname + ' does not have an _initialize_self function')
    except Exception as ex:
        ut.printex(ex, 'Error Reloading Class', keys=[
            'modname', 'module', 'class_', 'class_list', 'self', ])
        raise