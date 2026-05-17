def has_access_api(f):
    if hasattr(f, '_permission_name'):
        permission_str = f._permission_name
    else:
        permission_str = f.__name__
    def wraps(self, *args, **kwargs):
        permission_str = PERMISSION_PREFIX + f._permission_name
        if self.appbuilder.sm.has_access(
                permission_str,
                self.__class__.__name__
        ):
            return f(self, *args, **kwargs)
        else:
            log.warning(
                LOGMSG_ERR_SEC_ACCESS_DENIED.format(
                    permission_str,
                    self.__class__.__name__
                )
            )
            response = make_response(
                jsonify(
                    {
                        'message': str(FLAMSG_ERR_SEC_ACCESS_DENIED),
                        'severity': 'danger'
                    }
                ),
                401
            )
            response.headers['Content-Type'] = "application/json"
            return response
    f._permission_name = permission_str
    return functools.update_wrapper(wraps, f)