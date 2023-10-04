import ast
from pathlib import Path
from typing import List

import pandas as pd

from dataloader.dataloader import DataLoaderBase
from entity.project import Project


class GitRankingCSVDataLoader(DataLoaderBase):
    def __init__(self, file_path: str | Path,
                 projects_path: str | Path,
                 languages: List[str] | str = None,
                 remote: str = 'https://github.com'):
        super().__init__(file_path)
        self.projects_path = Path(projects_path)
        self.remote = remote
        if languages is None:
            languages = []
        if isinstance(languages, str):
            languages = [languages]
        self.languages = languages

    def load(self):
        projects: List[Project] = []
        dataset = pd.read_csv(self.file_path)

        dataset['labels'] = dataset['labels'].apply(ast.literal_eval)
        dataset['language'] = dataset['language'].fillna('')
        if self.languages:
            dataset = dataset[dataset['language'].isin(self.languages)]
        for name, language, labels in zip(dataset['full_name'], dataset['language'], dataset['labels']):
            folder_name = name.replace("/", "|")
            projects.append(Project(name=folder_name,
                                    remote=f"{self.remote}/{name}",
                                    dev_labels=labels,
                                    dir_path=str(self.projects_path.joinpath(folder_name)),
                                    languages=[language.lower()])
                            )

        return projects
