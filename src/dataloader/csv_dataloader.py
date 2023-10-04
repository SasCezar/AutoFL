from typing import List

import pandas as pd

from dataloader.dataloader import DataLoaderBase
from entity.project import Project


class CSVProjectLoader(DataLoaderBase):
    def load(self):
        projects: List[Project] = []

        project_list = pd.read_csv(self.file_path)
        pass