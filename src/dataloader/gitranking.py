import ast
from pathlib import Path
from typing import List

import pandas as pd

from dataloader.dataloader import DataLoaderBase
from entity.project import Project


class GitRankingCSVDataLoader(DataLoaderBase):
    def __init__(self, path: str | Path,
                 languages: List[str] | str = None,
                 remote: str = 'https://github.com'):
        super().__init__(path)
        self.remote = remote
        if languages is None:
            languages = []
        if isinstance(languages, str):
            languages = [languages]
        self.languages = languages

    def load(self):
        projects: List[Project] = []
        dataset = pd.read_csv(self.path)

        dataset['labels'] = dataset['labels'].apply(ast.literal_eval)
        if self.languages:
            dataset = dataset[dataset['language'].isin(self.languages)]
        for name, language, labels in zip(dataset['full_name'], dataset['language'], dataset['labels']):
            projects.append(Project(name=name.replace("/", "|"),
                                    remote=f"{self.remote}/{name}",
                                    dev_labels=labels,
                                    dir_path=f'/home/sasce/PycharmProjects/AutoFL/data/out/{name.replace("/", "|")}',
                                    languages=[language.lower()])
                            )

        return projects
