import os

def rename_script(old_name, new_name):
    """Rename a script

    :param old_name: The current name of the script
    :type old_name: str
    :param new_name: The new name for the script
    :type new_name: str

    :rtype: None
    """
    os.rename(old_name, new_name)