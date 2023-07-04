import json

import pandas as pd

from entity.project import Project
from loader.loader import LoaderBase


class JSONProjectLoader(LoaderBase):
    def load(self):
        projects = []
        with open(self.path, 'rt') as inf:
            for line in inf:
                obj = json.loads(line)
                project = Project(**obj)

                projects.append(project)

        return projects


class CSVProjectLoader(JSONProjectLoader):
    def load(self):
        project_list = pd.read_csv(self.path)

