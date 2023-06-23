import os

from git import Repo

from entity.project import Project


class GitVCS:
    def __init__(self, project: Project):
        self.project = project

    def checkout(self, commit_id: str):
        self.repo.git.checkout(commit_id)

    def clone(self):
        if not os.path.exists(self.project.dir_path):
            Repo.clone_from(self.project.remote, self.project.dir_path)

    def commit_list(self):
        pass
