def ensure_compatible_admin(view):

    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            roles = user.roles.all()
            if len(roles) != 1:
                return HttpResponseForbidden('User must be in exactly one role.')
            role = roles[0]
            if role.name == 'prison-clerk':
                prisons = user.prisons.all()
                if len(prisons) != 1:
                    return HttpResponseForbidden('Prison-clerk must be assigned to exactly one prison.')
        return view(request, *args, **kwargs)
    return wrapper