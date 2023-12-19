from pathlib import Path
from typing import List, Iterable

import pandas as pd

from dataloader.dataloader import DataLoaderBase
from entity.project import Project, Version


class ZakiProjectLoader(DataLoaderBase):
    def find_projects(self, cfg: dict = None):
        pass

    def __init__(self, file_path: str | Path,
                 projects_path: str | Path):
        super().__init__()
        self.file_path = Path(file_path)
        self.projects_path = Path(projects_path)

    def load(self, projects_list: list[str] | list[Project] = None) -> Iterable[Project]:
        projects: List[Project] = []
        records = pd.read_csv(self.file_path).to_dict('records')
        for record in records:

            project = Project(name=record['name'],
                              remote=record['url'],
                              dir_path=str(self.projects_path.joinpath(record['name'])),
                              languages=['java'],
                              versions=[Version(
                                  commit_id=record['commit SHA'],
                              )])
            projects.append(project)
        return projects
