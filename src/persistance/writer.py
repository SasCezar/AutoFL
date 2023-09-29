from abc import ABC

from entity.project import Project


class WriterBase(ABC):
    def __init__(self):
        pass

    def write(self, project: Project):
        pass
