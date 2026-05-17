def delete_release(repo, release_id, user_token):
    # code to verify if user_token has push access to the repo
    if has_push_access(repo, user_token):
        # code to delete the release with release_id
        if delete_release_request(repo, release_id, user_token):
            return True
    return False
