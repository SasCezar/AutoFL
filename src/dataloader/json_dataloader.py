import json
from typing import List

from dataloader.dataloader import DataLoaderBase
from entity.project import Project


class JSONProjectLoader(DataLoaderBase):
    def load(self):
        projects: List[Project] = []
        with open(self.path, 'rt') as inf:
            for line in inf:
                obj = json.loads(line)
                project = Project(**obj)

                projects.append(project)

        return projects
