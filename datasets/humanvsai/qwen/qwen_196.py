def display_iframe_url(target, **kwargs):
    from IPython.display import IFrame
    return IFrame(target, **kwargs)

def iframe_url(target, width=600, height=400, **kwargs):
    """Display the contents of a URL in an IPython notebook.

    :param target: the target url.
    :type target: string
    :param width: the width of the iframe.
    :type width: int
    :param height: the height of the iframe.
    :type height: int

    .. seealso:: `display_iframe_url()` for additional arguments."""
    from IPython.display import IFrame
    return IFrame(target, width, height, **kwargs)