from abc import ABC
from typing import List

from git import Repo


class LatestVersionStrategy(ABC):
    def get_versions(self, repository: Repo) -> List[str]:
        commits = list(repository.iter_commits('--all'))

        return [commits[0].hexsha]