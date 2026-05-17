def build_pdf(path_jinja2, template_name, path_outfile, template_kwargs=None):
    import os
    import jinja2
    import subprocess
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(path_jinja2))
    template = env.get_template(template_name)
    rendered_latex = template.render(template_kwargs or {})
    with open('temp.tex', 'w') as f:
        f.write(rendered_latex)
    subprocess.run(['pdflatex', 'temp.tex'], check=True)
    os.rename('temp.pdf', path_outfile)
    os.remove('temp.tex')
    os.remove('temp.pdf')