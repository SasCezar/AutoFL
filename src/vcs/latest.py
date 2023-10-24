from typing import List

from git import Repo

from entity.project import Version
from vcs.version_strategy import VersionStrategyBase


class LatestVersionStrategy(VersionStrategyBase):
    """
    Strategy to get the latest version of a project from a VCS repository (e.g. git)
    """
    def get_versions(self, repository: Repo) -> List[Version]:
        commits = list(repository.iter_commits('--all'))
        commit = commits[0]

        return [Version(commit_id=commit.hexsha, commit_num=len(commits),
                        commit_date=commit.committed_datetime, files=None)]
