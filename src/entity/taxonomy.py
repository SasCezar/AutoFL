import glob
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict

import pandas as pd


class Taxonomy(ABC):
    def __init__(self, path):
        self.path = path
        self.taxonomy: Dict[str, Label] = None
        self.inverted: Dict[int: Label] = None

    @abstractmethod
    def load(self):
        pass

    def __getitem__(self, item):
        return self.taxonomy[item]

    def get_label(self, index):
        return self.inverted[index]


@dataclass
class Label(ABC):
    index: int
    label: str


class GitRanking(Taxonomy):
    def __int__(self, path, keywords_path):
        super().__init__(path)
        self.keywords_path: str = keywords_path
        self.load()

    def load(self):
        """
        Loads the taxonomy labels with the keywords and weights
        :return:
        """
        with open(self.path, 'rt') as inf:
            labels = json.load(inf)

        keywords_files = [Path(x) for x in glob.glob(f"{self.keywords_path}/*.txt")]
        keywords = {}
        weights = {}
        for file in keywords_files:
            kw_weight = zip(pd.read_csv(file)['keyword'], pd.read_csv(file)['tfidf'])
            keywords[file.stem] = [kw for kw, _ in kw_weight]
            for kw, w in kw_weight:
                weights[file.stem][kw] = w

        for name, idx in labels.items():
            label = GitRankingLabel(index=idx, label=name, keywords=keywords[name], weights=weights[name])
            self.taxonomy[name] = label
            self.inverted[idx] = label


@dataclass
class GitRankingLabel(Label):
    index: int
    label: str
    keywords: List[str]
    weights: Dict[str, float]
