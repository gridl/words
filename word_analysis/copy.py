from git import Repo


def copy_repository(url, tmp_path='tmp/'):
    new_repo = Repo.init(tmp_path)
    origin = new_repo.create_remote('tmp', url)
    assert origin.exists()
    assert origin == new_repo.remotes.tmp == new_repo.remotes['tmp']
    origin.fetch()
    new_repo.create_head('master', origin.refs.master)
    new_repo.heads.master.set_tracking_branch(origin.refs.master)
    new_repo.heads.master.checkout()
    return tmp_path

if __name__ == "__main__":
    path = input("Enter the path of your project: ")
    copy_repository(path)