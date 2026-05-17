def comment_out_line(filename, line, comment='#',
                     update_or_append_line=update_or_append_line):
    update_or_append_line(filename, prefix=line, new_line=comment+line,
                          append=False)