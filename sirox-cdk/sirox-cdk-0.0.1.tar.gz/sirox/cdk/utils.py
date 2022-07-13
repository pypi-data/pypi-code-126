import git


def get_branch_commit() -> str:
    """ returns string composed by <branch_name>?<commit_hash> """
    repo = git.Repo(search_parent_directories=True)
    commit_sha = repo.head.object.hexsha[:7]
    branch_name = repo.active_branch.name
    return f"{branch_name}?{commit_sha}"
