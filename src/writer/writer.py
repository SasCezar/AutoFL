from abc import ABC
from typing import List

from entity.project import Project


class WriterBase(ABC):
    def __init__(self):
        pass

    def write(self, project: Project):
        pass

    def write_bulk(self, projects: List[Project]):
        pass
