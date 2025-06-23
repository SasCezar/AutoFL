from abc import ABC

from entity.project import Project


class ExecutionBase(ABC):
    def run(self, project: Project) -> Project:
        pass
