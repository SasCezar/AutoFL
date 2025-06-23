from pathlib import Path
from typing import List, Iterable

import pandas as pd

from dataloader.dataloader import DataLoaderBase
from entity.project import Project


class CSVProjectLoader(DataLoaderBase):
    def __init__(self, file_path: str | Path):
        super().__init__()
        self.file_path = Path(file_path)

    def load(
        self, projects_list: list[str] | list[Project] = None
    ) -> Iterable[Project]:
        projects: List[Project] = []
        project_list = pd.read_csv(self.file_path)
        projects = project_list["name"]
        return projects
