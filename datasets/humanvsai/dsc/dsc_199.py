import subprocess

def last_commit() -> Tuple:
    """Returns a tuple (hash, and commit object)"""
    git_log = subprocess.run(['git', 'log', '-1'], capture_output=True, text=True)
    commit_hash = git_log.stdout.split('\n')[0].split(' ')[1]
    commit_object = git_log.stdout.split('\n')[4].strip()
    return (commit_hash, commit_object)