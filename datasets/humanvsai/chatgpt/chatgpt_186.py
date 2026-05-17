import re

def get_sass_import_traceback(sass_file_path):
    """
    Return a `traceback` of Sass imports.
    """
    import_regex = r'@import\s+(?:(?:url\()?(?:(?:"|\')?)(.*?)(?:(?:"|\')?)\)?;)?'
    with open(sass_file_path, 'r') as sass_file:
        sass_content = sass_file.read()
    imports_list = re.findall(import_regex, sass_content)
    traceback = []
    for imported_file in imports_list:
        traceback.append(imported_file)
        inner_traceback = get_sass_import_traceback(imported_file)
        if len(inner_traceback) > 0:
            traceback.append('\t' + '\n\t'.join(inner_traceback))
    return traceback
