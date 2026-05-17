def last_commit(self) -> Tuple:
        from libs.repos import git
        return git.get_last_commit(repo_path=self.path)