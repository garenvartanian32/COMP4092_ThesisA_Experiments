def create(appname, **kwargs):
        if appname in LinkFactory._class_dict:
            return LinkFactory._class_dict[appname].create(**kwargs)
        else:
            raise KeyError(
                "Could not create object associated to app %s" % appname)