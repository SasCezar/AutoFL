from abc import ABC
from typing import List

from git import Repo


class FirstVersionStrategy(ABC):
    def get_versions(self, repository: Repo) -> List[str]:

        commits = list(repository.iter_commits('--all'))

        return [commits[-1].hexsha]
