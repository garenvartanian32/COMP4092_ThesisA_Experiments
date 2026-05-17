def p_include_file(p):
    global CURRENT_DIR
    p[0] = [p[1] + p[2]] + p[3] + [p[4]]
    CURRENT_FILE.pop()  # Remove top of the stack
    CURRENT_DIR = os.path.dirname(CURRENT_FILE[-1])