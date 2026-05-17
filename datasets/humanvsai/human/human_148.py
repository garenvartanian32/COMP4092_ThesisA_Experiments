def build_pdf(path_jinja2, template_name, path_outfile, template_kwargs=None):
    latex_template_object = LatexBuild(
            path_jinja2,
            template_name,
            template_kwargs,
            )
    return latex_template_object.build_pdf(path_outfile)