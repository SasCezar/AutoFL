import glob
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

import pandas as pd
from multiset import Multiset


@dataclass
class LabelBase(ABC):
    index: int
    name: str


@dataclass
class KeywordLabel(LabelBase):
    index: int
    name: str
    keywords: Multiset
    weights: Dict[str, float]


class TaxonomyBase(ABC):
    def __init__(self, path):
        self.path = path
        self.taxonomy: Dict[str, LabelBase] = None
        self.inverted: Dict[int: LabelBase] = None

        self.n = 0

    @abstractmethod
    def load(self):
        pass

    def __getitem__(self, item):
        return self.taxonomy[item]

    def get_label(self, index):
        return self.inverted[index]

    def __len__(self):
        return len(self.taxonomy)

    def __next__(self) -> LabelBase:
        if self.n <= len(self):
            self.n += 1
            return self.get_label(self.n)
        else:
            self.n = 0
            raise StopIteration


class KeywordTaxonomy(TaxonomyBase):
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
            keywords[file.stem] = Multiset([kw for kw, _ in kw_weight])
            for kw, w in kw_weight:
                weights[file.stem][kw] = w

        for name, idx in labels.items():
            label = KeywordLabel(index=idx, name=name, keywords=keywords[name], weights=weights[name])
            self.taxonomy[name] = label
            self.inverted[idx] = label
