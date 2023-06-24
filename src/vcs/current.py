from abc import ABC
from typing import List

from git import Repo


class CurrentVersionStrategy(ABC):
    def get_versions(self, repository: Repo) -> List[str]:
        return [repository.commit().hexsha]
