def run_all_evals(models, treebanks, out_file, check_parse=False, print_freq_tasks=False):
    """
    Run an evaluation for each language with its specified models and treebanks.

    Parameters:
    models (list): A list of models to be evaluated.
    treebanks (list): A list of treebanks to be evaluated.
    out_file (str): The output file path.
    check_parse (bool): If True, check the parse. Default is False.
    print_freq_tasks (bool): If True, print the frequency of tasks. Default is False.

    Returns:
    None
    """
    # Your code here