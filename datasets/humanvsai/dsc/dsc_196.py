from IPython.display import IFrame

def display_iframe_url(target, width="100%", height=500):
    """Display the contents of a URL in an IPython notebook.
    
    :param target: the target url.
    :type target: string
    :param width: the width of the iframe.
    :type width: string
    :param height: the height of the iframe.
    :type height: int
    """
    return IFrame(target, width=width, height=height)

# Example usage:
display_iframe_url('https://www.google.com')