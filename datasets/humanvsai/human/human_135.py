def ensure_compatible_admin(view):
    def wrapper(request, *args, **kwargs):
        user_roles = request.user.user_data.get('roles', [])
        if len(user_roles) != 1:
            context = {
                'message': 'I need to be able to manage user accounts. '
                           'My username is %s' % request.user.username
            }
            return render(request, 'mtp_common/user_admin/incompatible-admin.html', context=context)
        return view(request, *args, **kwargs)
    return wrapper