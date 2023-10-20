from abc import ABC, abstractmethod
from typing import Iterable

from entity.project import Project


class DataLoaderBase(ABC):
    def __init__(self, cfg: dict = None):
        self._project_list = None

    @property
    def project_list(self):
        return self._project_list

    @abstractmethod
    def load(self, projects_list: list[str] | list[Project] = None) -> Iterable[Project]:
        pass
