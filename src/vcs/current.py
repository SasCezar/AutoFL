from typing import List

from git import Repo

from entity.project import Version
from vcs.version_strategy import VersionStrategyBase


class CurrentVersionStrategy(VersionStrategyBase):
    """
    Strategy to get the current version of a project from a VCS repository (e.g. git)
    """

    def get_versions(self, repository: Repo) -> List[Version]:
        commit = repository.commit().hexsha
        commit_num = [
            i
            for i, _ in enumerate(repository.iter_commits("--all"))
            if _.hexsha == commit
        ][0]
        return [
            Version(
                commit_id=commit,
                commit_num=commit_num,
                commit_date=repository.commit().committed_datetime,
                files=None,
            )
        ]
