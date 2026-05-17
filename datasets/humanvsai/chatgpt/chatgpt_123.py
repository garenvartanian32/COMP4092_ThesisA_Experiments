from django.conf import settings
from django.urls import reverse


def get_path_with_language(language):
    if getattr(settings, 'PAGE_USE_LANGUAGE_PREFIX', False):
        language_code = language + '/'
    else:
        language_code = ''
    url = reverse('your_view_name_here')
    path = url.split('/', 3)[3]
    return '/{}{}'.format(language_code, path)
