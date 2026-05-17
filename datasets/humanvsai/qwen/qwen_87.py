def _read_doc():
    import os
    import re
    docstring = None
    with open('pefile.py', 'r') as file:
        content = file.read()
        match = re.search('"""(.*?)"""', content, re.DOTALL)
        if match:
            docstring = match.group(1)
    return docstring

def _extract_summary(docstring):
    """Extract the summary part of the docstring."""
    if docstring:
        lines = docstring.split('\n')
        for line in lines:
            if line.strip():
                return line.strip()
    return None

def _extract_description(docstring):
    """Extract the description part of the docstring."""
    if docstring:
        lines = docstring.split('\n')
        found_summary = False
        description_lines = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:
                if not found_summary:
                    found_summary = True
                else:
                    description_lines.append(stripped_line)
        return ' '.join(description_lines)
    return None

def _extract_parameters(docstring):
    """Extract the parameters part of the docstring."""
    if docstring:
        lines = docstring.split('\n')
        parameters_start = None
        for (i, line) in enumerate(lines):
            if line.strip().startswith(':param'):
                parameters_start = i
                break
        if parameters_start is not None:
            parameters = []
            for line in lines[parameters_start:]:
                stripped_line = line.strip()
                if stripped_line.startswith(':param'):
                    (param_name, param_desc) = stripped_line.split(':', 2)[2].split(' ', 1)
                    parameters.append((param_name.strip(), param_desc.strip()))
                elif stripped_line.startswith(':'):
                    break
            return parameters
    return None

def _extract_returns(docstring):
    """Extract the returns part of the docstring."""