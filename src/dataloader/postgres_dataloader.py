import json
from typing import Iterable

import sqlalchemy
from dataloader.dataloader import DataLoaderBase
from entity.project import Project, Version


class PostgresProjectLoader(DataLoaderBase):
    def __init__(self, host, db, user, password):
        super().__init__()
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.engine = sqlalchemy.create_engine(
            f"postgresql+psycopg://{user}:{password}@{host}/{db}"
        )
        self.metadata = sqlalchemy.MetaData()
        self.projects = sqlalchemy.Table(
            "project", self.metadata, autoload_with=self.engine
        )

    def load(self, projects_list: list[str] = None) -> Iterable[Project]:
        """
        Executes sql alchemy query to load all projects from the database that are in the projects_list
        :param cfg:
        :param projects_list:
        :return:
        """
        if projects_list is not None:
            projects_list = {int(x) for x in projects_list}
            query = sqlalchemy.select(self.projects).where(
                (self.projects.c.id.in_(projects_list))
            )
        else:
            query = sqlalchemy.select(self.projects)
        with self.engine.connect() as conn:

            result = conn.execute(query)
            for row in result:
                proj = Project(**json.loads(row[5]))
                proj.versions = [Version(**json.loads(row[6]))]
                yield proj

    def find_projects(self, cfg: dict = None):
        """
        Executes sql alchemy query to load all projects from the database
        :return:
        """
        with self.engine.connect() as conn:
            if cfg is None:
                query = sqlalchemy.select(self.projects.c.id)
            else:
                query = sqlalchemy.select(self.projects.c.id).where(
                    self.projects.c.config == cfg
                )
            result = conn.execute(query)
            for row in result:
                yield row[0]

    def load_single(self, project: str, cfg: dict):
        """
        Executes sql alchemy query to load a single project and all versions from the database
        :param project:
        :param cfg:
        :return:
        """
        with self.engine.connect() as conn:
            query = sqlalchemy.select(self.projects).where(
                (self.projects.c.name == project) & (self.projects.c.config == cfg)
            )
            result = list(conn.execute(query))
            project = Project(**json.loads(result[0][5]))
            project.versions = []
            for row in result:
                project.versions.append(Version(**json.loads(row[6])))

            return project
