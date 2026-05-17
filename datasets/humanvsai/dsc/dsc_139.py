class RepoManager:
    def __init__(self):
        self.repos = []  # Assume this is a list of your repositories

    def delete_repo(self, repo_name=None, force=False, all=False):
        if all:
            if force:
                self.repos = []
            else:
                raise Exception("Cannot delete all repos without force")
        elif repo_name:
            if repo_name in self.repos:
                self.repos.remove(repo_name)
            elif not force:
                raise Exception(f"Repo {repo_name} not found")
        else:
            raise Exception("No repo name provided")