from abc import ABC
from typing import List

from git import Repo


class VersionStrategyBase(ABC):
    def get_versions(self, repository: Repo) -> List[str]:
        pass
