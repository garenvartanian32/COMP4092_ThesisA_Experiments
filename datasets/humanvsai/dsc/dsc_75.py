from django.shortcuts import render

def render_full(request, lodgeit_url=None):
    # Here you can handle the traceback info
    # For example, you can get the traceback info from the request object
    traceback_info = request.META.get('traceback_info')

    # Then you can pass the traceback info to the template
    return render(request, 'full_page.html', {'traceback_info': traceback_info})