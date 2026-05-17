import subprocess
import jinja2

def build_pdf_from_jinja2_template(path_jinja2, template_name, path_outfile, template_kwargs):
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(path_jinja2))
    template = environment.get_template(template_name)
    rendered_template = template.render(template_kwargs)

    pdflatex_cmd = ['pdflatex', '-jobname', path_outfile, '-halt-on-error']
    try:
        p = subprocess.Popen(pdflatex_cmd, stdin=subprocess.PIPE)
        p.communicate(input=rendered_template.encode('utf-8'))
        p.wait()
    except ValueError as e:
        print("Error while generating pdf.")
        raise e
