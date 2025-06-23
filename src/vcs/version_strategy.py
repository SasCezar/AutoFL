from abc import ABC
from typing import List

from git import Repo

from entity.project import Version


class VersionStrategyBase(ABC):
    """
    Common interface for version strategies. A version strategy is a strategy to get the versions of a project from a
    VCS repository (e.g. git).
    """

    def get_versions(self, repository: Repo) -> List[Version]:
        pass
