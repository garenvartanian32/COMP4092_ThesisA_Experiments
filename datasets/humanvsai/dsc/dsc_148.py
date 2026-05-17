import os
from jinja2 import Environment, FileSystemLoader
from latex import build_pdf

def build_pdf(path_jinja2, template_name, path_outfile, template_kwargs=None):
    # Create a Jinja2 environment
    env = Environment(loader=FileSystemLoader(path_jinja2))

    # Get the template
    template = env.get_template(template_name)

    # Render the template
    if template_kwargs:
        rendered_template = template.render(**template_kwargs)
    else:
        rendered_template = template.render()

    # Write the rendered template to a temporary LaTeX file
    with open('temp.tex', 'w') as f:
        f.write(rendered_template)

    # Build the PDF
    build_pdf('temp.tex', path_outfile)

    # Remove the temporary LaTeX file
    os.remove('temp.tex')