from typing import List

from pymongo import MongoClient

from entity.project import Project, ProjectRepository
from writer.writer import WriterBase


class MongoWriter(WriterBase):
    def __init__(self, host: str, db: str = 'development'):
        super().__init__()
        self.client = MongoClient(host)
        self.db = self.client[db]
        self.project_repository = ProjectRepository(database=self.db)

    def write(self, project: Project):
        print(project.model_dump_json(indent=2))
        self.project_repository.save(project)

    def write_bulk(self, projects: List[Project]):
        for project in projects:
            self.write(project)
        #self.project_repository.save_many(projects)
