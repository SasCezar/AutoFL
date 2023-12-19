from typing import List

from git import Repo

from entity.project import Version
from vcs.version_strategy import VersionStrategyBase


class NoopVersionStrategy(VersionStrategyBase):
    """
    Strategy to get the current version of a project from a VCS repository (e.g. git)
    """
    def get_versions(self, repository: Repo) -> List[Version]:
        return []
