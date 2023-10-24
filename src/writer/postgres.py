import copy
from typing import List

import sqlalchemy

from entity.project import Project
from writer.writer import WriterBase
from sqlalchemy.dialects.postgresql import insert


class PostgresWriter(WriterBase):
    def __init__(self, host, db, user, password):
        super().__init__()
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.engine = sqlalchemy.create_engine(f'postgresql+psycopg://{user}:{password}@{host}/{db}')
        #self.connection = self.engine.connect()
        self.metadata = sqlalchemy.MetaData()
        self.projects = sqlalchemy.Table('project', self.metadata,
                                         autoload_with=self.engine)

    def write(self, project: Project):
        with self.engine.connect() as conn:
            black_project = copy.deepcopy(project)
            black_project.versions = []
            for version in project.versions:
                value = {"name": project.name,
                         "version_sha": version.commit_id,
                         "version_num": 11,
                         "config": project.cfg,
                         "project": black_project.model_dump_json(),  # TODO: Exclude versions
                         "version": version.model_dump_json()}

                query = insert(self.projects).values(value).on_conflict_do_update(
                    index_elements=['name', 'version_sha', 'config'],
                    set_=value
                )
                conn.execute(query)
            conn.commit()

    def write_bulk(self, projects: List[Project]):
        for project in projects:
            self.write(project)
