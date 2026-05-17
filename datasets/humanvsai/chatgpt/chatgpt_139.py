import shutil
import os

def delete_repo(repo_name:str, force:bool=False, all:bool=False):
    if all:
        # Deletes all the contents in the current directory recursively
        shutil.rmtree(os.getcwd())
    else:
        try:
            # Deletes the specified repo
            shutil.rmtree(repo_name)
        except Exception as e:
            if force:
                # Deletes the specified repo regardless of errors
                shutil.rmtree(repo_name, ignore_errors=True)
            else:
                raise e
