import autopep8

def autofix_codeblock(codeblock):
    fixed_codeblock = autopep8.fix_code(codeblock)
    return fixed_codeblock