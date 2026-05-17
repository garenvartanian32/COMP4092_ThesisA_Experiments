import sass

def format_sass_stack(sass_file):
    """Return a "traceback" of Sass imports."""
    with open(sass_file, 'r') as f:
        sass_content = f.read()

    # Use libsass to parse the Sass file
    # This will give you a list of all the imports in the file
    imports = sass.compile(string=sass_content, output_style='nested')

    # Return the list of imports
    return imports