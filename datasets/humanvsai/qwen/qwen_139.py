def delete_repo(self, repo_name=None, force=False, all=False):
    if all:
        pass
    elif repo_name:
        pass
    else:
        raise ValueError('Either repo_name or all must be specified')