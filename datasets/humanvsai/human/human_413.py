def make_proxy_method(cls, name):
        i = cls()
        view = getattr(i, name)
        for decorator in cls.decorators:
            view = decorator(view)
        @functools.wraps(view)
        def proxy(**forgettable_view_args):
            # Always use the global request object's view_args, because they
            # can be modified by intervening function before an endpoint or
            # wrapper gets called. This matches Flask's behavior.
            del forgettable_view_args
            if hasattr(i, "before_request"):
                response = i.before_request(name, **request.view_args)
                if response is not None:
                    return response
            before_view_name = "before_" + name
            if hasattr(i, before_view_name):
                before_view = getattr(i, before_view_name)
                response = before_view(**request.view_args)
                if response is not None:
                    return response
            response = view(**request.view_args)
            # You can also return a dict or None, it will pass it to render
            if isinstance(response, dict) or response is None:
                response = response or {}
                if hasattr(i, "_renderer"):
                    response = i._renderer(response)
                else:
                    _template = build_endpoint_route_name(cls, view.__name__)
                    _template = utils.list_replace([".", ":"], "/", _template)
                    _template = "%s.%s" % (_template, cls.template_markup)
                    # Set the title from the nav title, if not set
                    _meta_title = getattr(g, "__META__", {}).get("title")
                    if (not _meta_title or _meta_title == "") and get_view_attr(view, "title"):
                        page_attr(title=get_view_attr(view, "title"))
                    response.setdefault("_template", _template)
                    response = i.render(**response)
            if not isinstance(response, Response):
                response = make_response(response)
            for ext in cls._ext:
                response = ext(response)
            after_view_name = "after_" + name
            if hasattr(i, after_view_name):
                after_view = getattr(i, after_view_name)
                response = after_view(response)
            if hasattr(i, "after_request"):
                response = i.after_request(name, response)
            return response
        return proxy