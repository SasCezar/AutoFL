import json
from pathlib import Path
from typing import List, Iterable

from dataloader.dataloader import DataLoaderBase
from entity.project import Project


class JSONProjectLoader(DataLoaderBase):
    def __init__(self, file_path: str | Path):
        super().__init__()
        self.file_path = Path(file_path)

    def load(
        self, projects_list: list[str] | list[Project] = None
    ) -> Iterable[Project]:
        projects: List[Project] = []
        with open(self.file_path, "rt") as inf:
            for line in inf:
                obj = json.loads(line)
                project = Project(**obj)

                projects.append(project)

        return projects
