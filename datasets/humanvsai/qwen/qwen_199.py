def last_commit(self) -> Tuple:
    return (self.repo.head.commit.hexsha, self.repo.head.commit)