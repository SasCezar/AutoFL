from abc import ABC
from typing import List

from entity.project import Project, Version


class DateRangeVersionStrategyBase(ABC):
    def get_versions(self, project: Project) -> List[Version]:
        pass
