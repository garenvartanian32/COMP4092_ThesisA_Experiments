import os

def save_file(f, full_path, rules):
    """
    Saves file f to full_path and set rules.
    
    Args:
    f (file): The file object of the file to be saved
    full_path (str): The full path where the file will be saved
    rules (str): The permission rules to be set
    
    Returns:
    None
    """
    with open(full_path, 'wb') as new_file:
        new_file.write(f.read())
        os.chmod(full_path, int(rules, 8))
