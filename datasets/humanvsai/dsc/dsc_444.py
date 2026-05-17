import autopep8

def autofix_codeblock(codeblock, max_line_len=80):
    """
    Uses autopep8 to format a block of code

    Example:
        >>> # DISABLE_DOCTEST
        >>> import utool as ut
        >>> codeblock = ut.codeblock(
            '''
            def func( with , some = 'Problems' ):


             syntax ='Ok'
             but = 'Its very messy'
             if None:
                    # syntax might not be perfect due to being cut off
                    ommiting_this_line_still_works=   True
            ''')
        >>> fixed_codeblock = ut.autofix_codeblock(codeblock)
        >>> print(fixed_codeblock)
    """
    fixed_codeblock = autopep8.fix_code(codeblock, options={'max_line_length': max_line_len})
    return fixed_codeblock