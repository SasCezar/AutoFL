import os

from git import Repo

from entity.project import Project


class VCS: 
    @staticmethod
    def checkout(repo: Repo, commit_id: str):
        repo.git.checkout(commit_id)

    @staticmethod
    def init(project: Project):
        if not os.path.exists(project.dir_path):
            repo = Repo.clone_from(project.remote, project.dir_path)
        else:
            repo = Repo(project.dir_path)

        return repo

