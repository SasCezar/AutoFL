import json
from typing import List

from dataloader.dataloader import DataLoaderBase
from entity.project import Project


class DBProjectLoader(DataLoaderBase):
    def load(self):
        projects: List[Project] = []
        # TODO
        return projects
