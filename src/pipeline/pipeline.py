from abc import ABC

from entity.project import Project


class PipelineBase(ABC):
    pass

    def run(self, project: Project):
        pass
