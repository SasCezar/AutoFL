from typing import Iterable

import sqlalchemy
from sqlalchemy.orm import Session

from dataloader.dataloader import DataLoaderBase
from entity.project import Project


class PostgresProjectLoader(DataLoaderBase):
    def __init__(self, host, db, user, password):
        super().__init__()
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.engine = sqlalchemy.create_engine(f'postgresql+psycopg://{user}:{password}@{host}/{db}')
        self.connection = self.engine.connect()
        self.metadata = sqlalchemy.MetaData()
        self.projects = sqlalchemy.Table('project', self.metadata,
                                         autoload_with=self.engine)
        self._project_list = self.find_projects()

    def load(self, projects_list: list[str] | list[Project] = None) -> Iterable[Project]:
        """
        Executes sql alchemy query to load all projects from the database that are in the projects_list
        :param projects_list:
        :return:
        """
        with Session(self.engine) as session:
            res = session.query(self.projects).filter(self.projects.name.in_(self.project_list))

        res = [Project(**x.project, versions=[x.version]) for x in res.all()]
        return res

    def find_projects(self):
        with Session(self.engine) as session:
            res = session.query(self.projects)
        return [(x.name, x.version_sha, x.config) for x in res.all()]
