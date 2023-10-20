from typing import Iterable

from dataloader.dataloader import DataLoaderBase
from entity.project import Project, ProjectRepository
from pymongo import MongoClient


class MongoDBProjectLoader(DataLoaderBase):
    def __init__(self, host, db='development', cfg: dict = None):
        super().__init__()
        self.client = MongoClient(host)
        self.db = self.client[db]
        self.project_repository = ProjectRepository(database=self.db)
        self.cfg = cfg
        self._project_list = self.project_repository.find_by({'cfg': self.cfg})

    def load(self, projects_list: list[str] | list[Project] = None) -> Iterable[Project]:
        return self.project_repository.find_by({'cfg': self.cfg, "_id": {"$in": projects_list}})
