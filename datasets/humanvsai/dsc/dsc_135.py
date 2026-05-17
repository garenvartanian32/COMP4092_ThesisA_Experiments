def ensure_compatible_admin(view):
    def wrapper(request, *args, **kwargs):
        # Check if the user is in exactly one role
        if request.user.is_authenticated:
            if request.user.groups.count() != 1:
                # Handle the case where the user is not in exactly one role
                # This could be as simple as redirecting to a different page
                return redirect('error_page')
        return view(request, *args, **kwargs)
    return wrapper