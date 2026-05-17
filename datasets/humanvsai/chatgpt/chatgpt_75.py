def render_html_with_traceback(traceback_info):
    """Render the Full HTML page with the traceback info."""
    # import necessary library
    from traceback import format_tb
    
    # create the traceback string using the imported library
    traceback_string = ''.join(format_tb(traceback_info))
    
    # construct the HTML page with the traceback string
    html_page = f"""
    <html>
        <head>
            <title>Traceback Info</title>
        </head>
        <body>
            <h1>Traceback:</h1>
            <p>{traceback_string}</p>
        </body>
    </html>
    """
    # return the HTML page
    return html_page
