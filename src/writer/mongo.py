from typing import List

from pymongo import MongoClient

from entity.project import Project, ProjectRepository
from writer.writer import WriterBase


class MongoWriter(WriterBase):
    def __init__(self, host: str):
        super().__init__()
        self.client = MongoClient(host)
        self.db = self.client['development']
        self.project_repository = ProjectRepository(database=self.db)

    def write(self, project: Project):
        self.project_repository.save(project)

    def write_bulk(self, projects: List[Project]):
        self.project_repository.save_many(projects)
