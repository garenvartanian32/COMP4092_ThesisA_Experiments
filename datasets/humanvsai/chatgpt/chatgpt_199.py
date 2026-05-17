import hashlib
import git

def get_commit_and_hash(repo_path):
    """
    Returns a tuple (hash, and commit object)
    """
    repo = git.Repo(repo_path)
    commit = repo.head.commit
    commit_hash = hashlib.sha1(bytes(commit.hexsha, 'ascii')).hexdigest()  
    return (commit_hash, commit)
