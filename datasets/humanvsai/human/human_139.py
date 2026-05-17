def delete_repo(self, repo_name=None, force=False, all=False):
        if not all:
            if repo_name:
                req = proto.DeleteRepoRequest(repo=proto.Repo(name=repo_name), force=force)
                self.stub.DeleteRepo(req, metadata=self.metadata)
            else:
                raise ValueError("Either a repo_name or all=True needs to be provided")
        else:
            if not repo_name:
                req = proto.DeleteRepoRequest(force=force, all=all)
                self.stub.DeleteRepo(req, metadata=self.metadata)
            else:
                raise ValueError("Cannot specify a repo_name if all=True")