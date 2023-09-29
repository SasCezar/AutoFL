from abc import ABC

from entity.project import Project


class DBWriter(ABC):
    def __init__(self, sql_db, exclude):
        self.sql_db = sql_db
        self.exclude = exclude

    def write(self, project: Project):
        project_dict = project.model_dump_json(exclude=self.exclude)
        pass
